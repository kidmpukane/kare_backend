from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import SkinProgram, CurrentProgram
from .serializers import SkinProgramSerializer, CurrentProgramSerializer


class ListAllProgramView(APIView):
    def get(self, request, format=None):
        program = SkinProgram.objects.all()
        serializer = SkinProgramSerializer(program, many=True)
        return Response(serializer.data)
    
class RecommendedProgramView(APIView):
    def get(self, request, format=None):
        predicted_skin_type = request.query_params.get("predicted_skin_type")

        if predicted_skin_type is None:
            return Response({"error": "predicted_skin_type query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            predicted_skin_type = int(predicted_skin_type)
        except ValueError:
            return Response({"error": "predicted_skin_type must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

        programs = SkinProgram.objects.filter(skin_type=predicted_skin_type)

        if not programs.exists():
            return Response({"error": "No programs found for this skin type"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SkinProgramSerializer(programs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)