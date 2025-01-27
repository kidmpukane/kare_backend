from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
from accounts.models import CustomUser
from rest_framework.permissions import AllowAny


class EditProfileView(APIView):
    def get(self, request, user_id, format=None):

        custom_user = CustomUser.objects.get(id=user_id)
        user_profile = custom_user.profile
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        custom_user = CustomUser.objects.get(id=user_id)
        user_profile = custom_user.profile
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchUserProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id, format=None):
        try:
            custom_user = CustomUser.objects.get(id=user_id)
            user_profile = custom_user.profile
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


class ListAllProfilesView(APIView):
    def get(self, request, format=None):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)