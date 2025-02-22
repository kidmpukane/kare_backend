from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SkinRoutine, Instructions
from programs.models import SkinProgram
from .serializers import SkinRoutineSerializers, InstructionsSerializers
# Create your views here.


class ListAllRoutines(APIView):
    def get(self, request, format=None):
        routines = SkinRoutine.objects.all()
        serializer = SkinRoutineSerializers(routines, many=True)
        return Response(serializer.data)


class GetRoutinesByProgramID(APIView):
    def get(self, request, program_id):
        try:
            routines = SkinRoutine.objects.filter(programs__id=program_id)
            if not routines.exists():
                return Response(
                    {"message": "No routines found for this program."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = SkinRoutineSerializers(routines, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ListAllInstructions(APIView):
    def get(self, request, format=None):
        instructions = Instructions.objects.all()
        serializer = InstructionsSerializers(instructions, many=True)
        return Response(serializer.data)


class GetInstructionsByRoutineID(APIView):
    def get(self, request, routine_id):
        try:
            instructions = Instructions.objects.filter(
                routines__id=routine_id)  # 🔥 FIXED

            if not instructions.exists():
                return Response(
                    {"message": "No instructions found for this routine."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = InstructionsSerializers(instructions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
