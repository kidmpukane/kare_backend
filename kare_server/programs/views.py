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
    
class FilterProgramView(APIView):
    def get(self, request, skin_type, format=None):
        try:
            programs = SkinProgram.objects.filter(skin_type=skin_type)
            serializer = SkinProgramSerializer(programs, many=True)
            return Response(serializer.data)
        except SkinProgram.DoesNotExist:
            return Response({'error': 'Program does not exist'}, status=status.HTTP_404_NOT_FOUND)
