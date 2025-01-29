from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import NormalSkinProgram, OilySkinProgram, DrySkinProgram, CombinationSkinProgram, SensitiveSkinProgram
from .serializers import NormalSkinProgramSerializer, OilySkinProgramSerializer, DrySkinProgramSerializer, CombinationSkinProgramSerializer, SensitiveSkinProgramSerializer



SKIN_TYPE_PROGRAMS = {
    0: NormalSkinProgram,
    1: OilySkinProgram,
    2: DrySkinProgram,
    3: CombinationSkinProgram,
    4: SensitiveSkinProgram,
}

def get_program_by_skin_type(skin_type):
    model = SKIN_TYPE_PROGRAMS.get(skin_type)
    return model.objects.first() if model else None

@csrf_exempt
def get_recommended_program(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            skin_type = data.get("skin_type")

            if skin_type is None or skin_type not in SKIN_TYPE_PROGRAMS:
                return JsonResponse({"error": "Invalid or missing skin_type"}, status=400)

            program = get_program_by_skin_type(skin_type)

            if not program:
                return JsonResponse({"error": "No program found for this skin type"}, status=404)

            return JsonResponse({
                "name": program.name,
                "description": program.description,
                "duration": program.duration,
            })
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    elif request.method == "GET":  # Allow testing with GET
        return JsonResponse({"message": "Use POST with { 'skin_type': X }"}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)

class ListAllProgramView(APIView):
    def get(self, request, format=None):
        program = NormalSkinProgram.objects.all()
        serializer = NormalSkinProgramSerializer(program, many=True)
        return Response(serializer.data)