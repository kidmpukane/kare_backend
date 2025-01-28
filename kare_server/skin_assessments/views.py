from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserSkinAssessmentResults
from .serializers import UserSkinAssessmentResultsSerializer, PredictRequestSerializer
from ml_models.models.ffnn_model import predict_skin_type
from products.models import Products
from programs.models import Programs


class PredictSkinAPIView(APIView):
    def post(self, request):
        serializer = PredictRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz_answers = serializer.validated_data['quiz_answers']

        # Predict skin type
        predicted_skin_type = predict_skin_type(quiz_answers)

        # Filter products and programs based on the predicted skin type
        products = Products.objects.filter(skin_types__icontains=predicted_skin_type)
        programs = Programs.objects.filter(skin_types__icontains=predicted_skin_type)

        # Serialize the products and programs
        recommended_products = [
            {"name": product.name, "description": product.description, "price": product.price}
            for product in products
        ]
        recommended_programs = [
            {"name": program.name, "description": program.description, "duration": program.duration}
            for program in programs
        ]

        # Save the results in the database
        user = request.user.profile  # Assuming the request has the user's profile
        skin_assessment_result, created = UserSkinAssessmentResults.objects.update_or_create(
            user_name=user,
            defaults={
                "skin_type": predicted_skin_type,
                "recommended_products": recommended_products,
                "recommended_programs": recommended_programs,
            },
        )

        # Serialize the response
        results_serializer = UserSkinAssessmentResultsSerializer(skin_assessment_result)

        return Response({
            'predicted_skin_type': predicted_skin_type,
            'filtered_products': recommended_products,
            'filtered_programs': recommended_programs,
            'assessment_results': results_serializer.data
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
