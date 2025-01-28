from rest_framework.response import Response
from rest_framework.views import APIView
from .models.programs import (
    DrySkinProgram,
    OilySkinProgram,
    CombinationSkinProgram,
    SensitiveSkinProgram,
    NormalSkinProgram,
)


class RecommendProgramView(APIView):
    def get_program_for_skin_type(self, skin_type):
        if skin_type == "Dry":
            return DrySkinProgram.objects.first()
        elif skin_type == "Oily":
            return OilySkinProgram.objects.first()
        elif skin_type == "Combination":
            return CombinationSkinProgram.objects.first()
        elif skin_type == "Sensitive":
            return SensitiveSkinProgram.objects.first()
        elif skin_type == "Normal":
            return NormalSkinProgram.objects.first()
        else:
            return None

    def post(self, request):
        skin_type = request.data.get("skin_type")
        program = self.get_program_for_skin_type(skin_type)

        if program:
            return Response(
                {
                    "skin_type": skin_type,
                    "program": {
                        "name": program.name,
                        "description": program.description,
                        "duration": program.duration,
                    },
                }
            )
        else:
            return Response(
                {"error": "No program found for the specified skin type."},
                status=404,
            )
