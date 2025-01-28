from rest_framework import serializers
from .models import (
    CurrentProgram,
    DrySkinProgram,
    OilySkinProgram,
    CombinationSkinProgram,
    SensitiveSkinProgram,
    NormalSkinProgram,
)


# Serializers for Hardcoded Programs
class DrySkinProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrySkinProgram
        fields = "__all__"


class OilySkinProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilySkinProgram
        fields = "__all__"


class CombinationSkinProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombinationSkinProgram
        fields = "__all__"


class SensitiveSkinProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensitiveSkinProgram
        fields = "__all__"


class NormalSkinProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalSkinProgram
        fields = "__all__"


# Serializer for Current Program
class CurrentProgramSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display the user's name/identifier

    class Meta:
        model = CurrentProgram
        fields = ["user", "current_program", "start_date", "end_date"]
