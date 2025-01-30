from django.urls import path
from .views import ListAllProgramView as list_all_program_view, FilterProgramView as filter_program_view

urlpatterns = [
    path("filter-programs/<str:skin_type>/", filter_program_view.as_view(), name="filter_program"),
    path("programs/", list_all_program_view.as_view(), name="list_all_programs"),
]
