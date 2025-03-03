from django.urls import path
from .views import (ListAllProgramView as list_all_program_view, FilterProgramView as filter_program_view, CreateProgramView as create_program,
                    CreateCurrentProgramView as create_current_program, GetCurrentProgramView as get_current_program,
                    RetrieveProgramView as retrieve_program, UpdateProgramView as update_program,
                    PartialUpdateProgramView as partial_update_program, DeleteProgramView as delete_program
                    )

urlpatterns = [
    path("filter-programs/<str:skin_type>/",
         filter_program_view.as_view(), name="filter_program"),
    path("programs/", list_all_program_view.as_view(), name="list_all_programs"),
    path("create-program/", create_program.as_view(), name="create_program"),
    path("create-current-program/", create_current_program.as_view(),
         name="create-current-program"),
    path("retrieve-program/<str:program_id>/", retrieve_program.as_view(),
         name="retrieve-program"),
    path("update-program/<str:program_id>/", update_program.as_view(),
         name="update-program"),
    path("partially-update-program/<str:program_id>/", partial_update_program.as_view(),
         name="partially_update_program"),
    path("delete-program/<str:program_id>/", delete_program.as_view(),
         name="delete-program"),

]
