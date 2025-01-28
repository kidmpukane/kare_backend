from django.db import models
from django_random_id_model import RandomIDModel
from user_profiles.models import UserProfile


class UserSkinAssessmentResults(RandomIDModel):
    user_name = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name='AssessmentOwner'
    )
    skin_type = models.CharField(max_length=500, default='Default Skin Type')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_name} - {self.skin_type}"
