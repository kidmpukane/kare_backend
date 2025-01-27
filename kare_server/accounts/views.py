import logging
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework import permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from .models import CustomUser
from .serializers import CustomUserSerializer
from softdelete.models import SoftDeleteObject
from user_profiles.models import UserProfile


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        csrf_token = get_token(request)
        response_data = {'success': 'CSRF cookie set',
                         'csrf_token': csrf_token}
        return JsonResponse(response_data)


logger = logging.getLogger(__name__)


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = request.data

        email = data['email']
        password = data['password']
        re_password = data['re_password']

        if not email or not password or not re_password:
            return Response({'error': 'Email, password, and re_password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if password != re_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 6:
            return Response({'error': 'Password must be at least 6 characters'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.create_user(
                email=email, password=password)

            # Create UserProfile instance for the user
            UserProfile.objects.create(
                user=user,
                user_name="enter_username"
            )

            # Authenticate the user
            auth_user = authenticate(request, email=email, password=password)

            if auth_user is None:
                logger.error("User authentication failed.")
                return Response({'error': 'User authentication failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            login(request, auth_user)

            csrf_token = get_token(request)
            request.session['csrf_token'] = csrf_token

            # Return the CSRF token, session ID, email, and user ID in the response
            return Response({
                'success': 'User created and logged in successfully',
                'csrf_token': csrf_token,
                'sessionid': request.session.session_key,
                'email': auth_user.email,
                'user_id': auth_user.id,
            })

        except Exception as e:
            logger.exception("Error occurred during user registration: %s", e)
            return Response({'error': f'Something went wrong when registering account: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = request.data

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)

                # Generate CSRF token and add it to the session
                csrf_token = get_token(request)
                request.session['csrf_token'] = csrf_token

                # Return the CSRF token, session ID, email, user ID, and is_merchant in the response
                return Response({
                    'success': 'User authenticated',
                    'csrf_token': csrf_token,
                    'sessionid': request.session.session_key,
                    'email': user.email,
                    'user_id': user.id,
                })
            else:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': f'Something went wrong when logging in: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --------------------------------------------GET USER----------------------------------------------


@api_view(['GET'])
def get_user_by_id(request, id):
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

# --------------------------------------------LOGIN USER----------------------------------------------


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            logout(request)
            return Response({'success': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Something went wrong when logging out: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            logout(request)
            return Response({'success': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Something went wrong when logging out: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --------------------------------------------PASSWORD RESET----------------------------------------------


class PasswordResetView(APIView):
    pass

# --------------------------------------------PASSWORD RETRIEVAL----------------------------------------------


class PasswordRetrievalView(APIView):
    pass

# --------------------------------------------SOCIAL AUTH VIEW---------------------------------------------


class SocialAuthenticationView(APIView):
    pass

# --------------------------------------------DELETE ACCOUNT VIEW---------------------------------------------


class DeleteAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, id=user_id)

            if hasattr(user, 'delete') and callable(getattr(user, 'delete')):
                # Soft delete the user using the softdelete library
                user.delete()
            else:
                # Fallback to setting is_active to False
                user.is_active = False
                user.save()

            logout(request)
            return Response({'success': 'Account deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Something went wrong when deleting the account: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --------------------------------------------DELETE ACCOUNT VIEW---------------------------------------------


class GetUserByIdView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# --------------------------------------------DELETE ACCOUNT VIEW---------------------------------------------


class DeleteUserByIdView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)