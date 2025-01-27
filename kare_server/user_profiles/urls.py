from django.urls import path
from .views import EditProfileView, FetchUserProfileView, ListAllProfilesView

urlpatterns = [
    path('edit-profile/<int:user_id>/',
         EditProfileView.as_view(), name='edit-profile'),
    path('fetch-user-profile/<int:user_id>/',
         FetchUserProfileView.as_view(), name='fetch-user-profile'),
    path('all-profiles/', ListAllProfilesView.as_view(), name='all-profiles'),
]