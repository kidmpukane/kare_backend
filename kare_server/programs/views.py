from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NormalSkinProgram, OilySkinProgram, DrySkinProgram, CombinationSkinProgram, SensitiveSkinProgram

# Mapping skin type to corresponding model
SKIN_TYPE_PROGRAMS = {
    0: NormalSkinProgram,
    1: OilySkinProgram,
    2: DrySkinProgram,
    3: CombinationSkinProgram,
    4: SensitiveSkinProgram,
}

# Function to fetch program based on skin type
def get_program_by_skin_type(skin_type):
    model = SKIN_TYPE_PROGRAMS.get(skin_type)
    if model:
        return model.objects.first()  # Assuming only one instance per skin type
    return None

@csrf_exempt  # Disable CSRF for testing with tools like Postman
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

    return JsonResponse({"error": "Invalid request method"}, status=405)
