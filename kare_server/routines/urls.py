from django.urls import path
from .views import ListAllRoutines as list_all_routines, ListAllInstructions as list_all_instructions

urlpatterns = [
    path("all_routines", list_all_routines.as_view(), name="all_routines"),
    path("all_instructions", list_all_instructions.as_view(),
         name="all_instructions"),
]
