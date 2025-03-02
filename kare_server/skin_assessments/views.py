from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserSkinAssessmentResults
from .serializers import PredictRequestSerializer, UserSkinAssessmentResultsSerializer
from user_profiles.models import UserProfile
from ml_models.models.ffnn_model import predict_skin_type

# Mock function for predicting skin type (replace with actual implementation)


# def predict_skin_type(quiz_answers):
#     # This is a placeholder for the ML model or logic used to predict the skin type.
#     return 1  # Replace with your actual prediction logic


class PredictSkinAPIView(APIView):
    def post(self, request):
        # Validate the incoming request data
        serializer = PredictRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz_answers = serializer.validated_data['quiz_answers']

        # Predict the skin type
        predicted_skin_type = predict_skin_type(quiz_answers)

        # Get the user's profile (ensure the user is authenticated)
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "User profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Save the results in the database, also saving the user_id
        skin_assessment_result, created = UserSkinAssessmentResults.objects.update_or_create(
            user_name=user_profile,
            defaults={
                "skin_type": predicted_skin_type,
            },
        )

        # Serialize and return the saved results
        results_serializer = UserSkinAssessmentResultsSerializer(
            skin_assessment_result)
        return Response({
            "predicted_skin_type": predicted_skin_type,
            "assessment_results": results_serializer.data,
        }, status=status.HTTP_201_CREATED)


class FetchAssessmentByUserIdView(APIView):
    def get(self, request, user_id, format=None):
        try:
            user_profile = UserProfile.objects.get(id=user_id)
            skin_assessment_results = UserSkinAssessmentResults.objects.filter(
                user_name=user_profile)
            serializer = UserSkinAssessmentResultsSerializer(
                skin_assessment_results, many=True)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except UserSkinAssessmentResults.DoesNotExist:
            return Response({'error': 'No skin assessment results found for this user'}, status=status.HTTP_404_NOT_FOUND)


class FetchAllAssessmentsView(APIView):
    def get(self, request, format=None):
        skin_assessment_results = UserSkinAssessmentResults.objects.all()
        serializer = UserSkinAssessmentResultsSerializer(
            skin_assessment_results, many=True)
        return Response(serializer.data)
