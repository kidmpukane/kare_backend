from django.db import models
from django_random_id_model import RandomIDModel
from accounts.models import CustomUser


class UserProfile(RandomIDModel):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to='images/', null=True, blank=True, default=".")
    user_name = models.CharField(max_length=100, default="no-username")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_name}"