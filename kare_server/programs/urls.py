from django.urls import path
from .views import ListAllProgramView as list_all_program_view, FilterProgramView as filter_program_view, CreateCurrentProgramView as create_current_program, GetCurrentProgramView as get_current_program

urlpatterns = [
    path("filter-programs/<str:skin_type>/", filter_program_view.as_view(), name="filter_program"),
    path("programs/", list_all_program_view.as_view(), name="list_all_programs"),
    path("create-current-program/", create_current_program.as_view(), name="create_current_program"),
    path("get-current-program/", get_current_program.as_view(), name="get-current-program")
]
