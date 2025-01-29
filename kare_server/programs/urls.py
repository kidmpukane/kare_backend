from django.urls import path
from .views import get_recommended_program, ListAllProgramView as list_all_program_view

urlpatterns = [
    path("recommended-program/", get_recommended_program, name="recommended_program"),
    path("programs/", list_all_program_view.as_view(), name="list_all_programs"),
]
