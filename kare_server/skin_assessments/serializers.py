from rest_framework import serializers
from .models import UserSkinAssessmentResults


class UserSkinAssessmentResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkinAssessmentResults
        fields = '__all__'


class PredictRequestSerializer(serializers.Serializer):
    quiz_answers = serializers.ListField(
        child=serializers.FloatField(),
        help_text="List of quiz answers used to predict skin type."
    )
