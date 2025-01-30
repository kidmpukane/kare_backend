from rest_framework import serializers
from .models import (
    CurrentProgram,
    SkinProgram
)


# Serializers for Hardcoded Programs
class SkinProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinProgram
        fields = "__all__"

# Serializer for Current Program
class CurrentProgramSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display the user's name/identifier

    class Meta:
        model = CurrentProgram
        fields = ["user", "current_program", "start_date", "end_date"]
