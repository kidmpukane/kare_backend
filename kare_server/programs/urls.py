from django.urls import path
from .views import get_recommended_program

urlpatterns = [
    path("recommended-program/", get_recommended_program, name="recommended_program"),
]
