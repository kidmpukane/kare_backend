from django.db import models
from user_profiles.models import UserProfile

class CurrentProgram(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="current_program")
    current_program = models.CharField(max_length=255, default="None")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}'s Current Program: {self.current_program}"

class SkinProgram(models.Model):
    name = models.CharField(max_length=255, default="Hydration Boost Program")
    description = models.TextField(
        default="A 4-week program designed to restore moisture levels and improve the skin barrier for dry skin."
    )
    duration = models.CharField(max_length=50, default="4 weeks")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=49.99)
    image = models.ImageField(upload_to="images/")
    skin_type = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return self.name