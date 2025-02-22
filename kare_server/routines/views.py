from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SkinRoutine, Instructions
from .serializers import SkinRoutineSerializers, InstructionsSerializers
# Create your views here.


class ListAllRoutines(APIView):
    def get(self, request, format=None):
        routines = SkinRoutine.objects.all()
        serializer = SkinRoutineSerializers(routines, many=True)
        return Response(serializer.data)


class ListAllInstructions(APIView):
    def get(self, request, format=None):
        instructions = Instructions.objects.all()
        serializer = SkinRoutineSerializers(instructions, many=True)
        return Response(serializer.data)
