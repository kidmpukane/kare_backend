from django.urls import path
from .views import (
    GetCSRFToken,
    RegistrationView,
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordRetrievalView,
    SocialAuthenticationView,
    DeleteAccountView,
    GetUserByIdView,
    DeleteUserByIdView

)


urlpatterns = [

    path('csrf_cookie/', GetCSRFToken.as_view()),
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-retrieval/', PasswordRetrievalView.as_view()),
    path('social-authentication/', SocialAuthenticationView.as_view()),
    path('delete-account/<int:user_id>/',
         DeleteAccountView.as_view(), name='delete-account'),
    path('users/<int:id>/', GetUserByIdView.as_view(), name='get-user-by-id'),
    path('delete-users/<int:id>/', DeleteUserByIdView.as_view(),
         name='delete-user-by-id'),

]