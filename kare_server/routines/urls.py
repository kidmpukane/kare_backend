from django.urls import path
from .views import ListAllRoutines as list_all_routines, ListAllInstructions as list_all_instructions, GetRoutinesByProgramID as get_routines_by_programs, GetInstructionsByRoutineID as get_instructions_by_routines

urlpatterns = [
    path("all_routines", list_all_routines.as_view(), name="all_routines"),
    path("all_instructions", list_all_instructions.as_view(),
         name="all_instructions"),
    path("get_routines_by_programs/<int:program_id>/", get_routines_by_programs.as_view(),
         name="get_routines_by_programs"),
    path("get_instructions_by_routines/<int:routine_id>/", get_instructions_by_routines.as_view(),
         name="get_instructions_by_routines"),
]
