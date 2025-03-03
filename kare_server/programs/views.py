from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_profiles.models import UserProfile
from user_profiles.serializers import UserProfileSerializer
from .models import SkinProgram, CurrentProgram
from .serializers import SkinProgramSerializer, CurrentProgramSerializer

# <------------------------------------------------------------------------------------------------------------------>
# <----------------------------------------------------Program------------------------------------------------------->
# <------------------------------------------------------------------------------------------------------------------>


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


class CreateProgramView(APIView):
    def post(self, request, format=None):
        serializer = SkinProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveProgramView(APIView):

    def get(self, request, program_id, format=None):
        try:
            program = SkinProgram.objects.get(id=program_id)
            serializer = SkinProgramSerializer(program)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SkinProgram.DoesNotExist:
            return Response({'error': 'Program does not exist'}, status=status.HTTP_404_NOT_FOUND)


class UpdateProgramView(APIView):

    def put(self, request, program_id, format=None):
        try:
            program = SkinProgram.objects.get(id=program_id)
            serializer = SkinProgramSerializer(program, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SkinProgram.DoesNotExist:
            return Response({'error': 'Program does not exist'}, status=status.HTTP_404_NOT_FOUND)


class PartialUpdateProgramView(APIView):

    def patch(self, request, program_id, format=None):
        try:
            program = SkinProgram.objects.get(id=program_id)
            serializer = SkinProgramSerializer(
                program, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SkinProgram.DoesNotExist:
            return Response({'error': 'Program does not exist'}, status=status.HTTP_404_NOT_FOUND)


class DeleteProgramView(APIView):

    def delete(self, request, program_id, format=None):
        try:
            program = SkinProgram.objects.get(id=program_id)
            program.delete()
            return Response({'message': 'Program deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except SkinProgram.DoesNotExist:
            return Response({'error': 'Program does not exist'}, status=status.HTTP_404_NOT_FOUND)
# <------------------------------------------------------------------------------------------------------------------>
# <-------------------------------------------------Current Program-------------------------------------------------->
# <------------------------------------------------------------------------------------------------------------------>


class CreateCurrentProgramView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get("user_id")
        program_ids = request.data.get("program_ids", [])

        try:
            user_profile = UserProfile.objects.get(id=user_id)
            programs = SkinProgram.objects.filter(id__in=program_ids)

            if not programs.exists():
                return Response({"error": "No valid programs found"}, status=status.HTTP_400_BAD_REQUEST)

            current_program, created = CurrentProgram.objects.get_or_create(
                user=user_profile)
            current_program.current_program.set(
                programs)  # Assign multiple programs
            current_program.save()

            serializer = CurrentProgramSerializer(current_program)
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


class GetCurrentProgramView(APIView):
    def get(self, request, user_id, format=None):
        try:
            current_program = CurrentProgram.objects.get(user__id=user_id)
            serializer = CurrentProgramSerializer(current_program)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CurrentProgram.DoesNotExist:
            return Response({"error": "No current program found for this user"}, status=status.HTTP_404_NOT_FOUND)
