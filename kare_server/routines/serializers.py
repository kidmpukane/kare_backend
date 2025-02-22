from rest_framework import serializers
from .models import (
    SkinRoutine,
    Instructions
)


class SkinRoutineSerializers(serializers.ModelSerializer):
    class Meta:
        model = SkinRoutine
        fields = "__all__"


class InstructionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = "__all__"
