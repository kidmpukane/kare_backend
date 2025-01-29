from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserSkinAssessmentResults
from .serializers import PredictRequestSerializer, UserSkinAssessmentResultsSerializer
from user_profiles.models import UserProfile

# Mock function for predicting skin type (replace with actual implementation)
def predict_skin_type(quiz_answers):
    # This is a placeholder for the ML model or logic used to predict the skin type.
    return "dry"  # Replace with your actual prediction logic

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
        results_serializer = UserSkinAssessmentResultsSerializer(skin_assessment_result)
        return Response({
            "predicted_skin_type": predicted_skin_type,
            "assessment_results": results_serializer.data,
        }, status=status.HTTP_201_CREATED)


# class PredictSkin(APIView):
#   def post(self, request):
#       serializer = PredictRequestSerializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       quiz_answers = serializer.validated_data['quiz_answers']
#       predicted_skin_type = predict_skin_type(quiz_answers)

#       # Get all products
#       products = Products.objects.all()

#       # Filter products by the predicted skin type
#       filtered_products = products.filter(skin_type=predicted_skin_type)

#       # Return the filtered products
#       product_serializer = ProductSerializer(filtered_products, many=True)
#       return Response(product_serializer.data)
