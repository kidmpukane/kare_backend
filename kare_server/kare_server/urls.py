from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/user_profiles/', include('user_profiles.urls')),
    # path('api/skin_assessments/', include('skin_assessments.urls')),
]
