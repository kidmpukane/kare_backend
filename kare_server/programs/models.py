from django.db import models


class DrySkinProgram(models.Model):
    name = models.CharField(max_length=255, default="Hydration Boost Program")
    description = models.TextField(
        default="A 4-week program designed to restore moisture levels and improve the skin barrier for dry skin."
    )
    duration = models.CharField(max_length=50, default="4 weeks")

    def __str__(self):
        return self.name


class OilySkinProgram(models.Model):
    name = models.CharField(max_length=255, default="Oil Control Regimen")
    description = models.TextField(
        default="A 3-week program focusing on reducing excess sebum and preventing clogged pores for oily skin."
    )
    duration = models.CharField(max_length=50, default="3 weeks")

    def __str__(self):
        return self.name


class CombinationSkinProgram(models.Model):
    name = models.CharField(max_length=255, default="Balanced Skin Care Routine")
    description = models.TextField(
        default="A 2-week program to balance hydration and oil production for combination skin."
    )
    duration = models.CharField(max_length=50, default="2 weeks")

    def __str__(self):
        return self.name


class SensitiveSkinProgram(models.Model):
    name = models.CharField(max_length=255, default="Gentle Skin Program")
    description = models.TextField(
        default="A 1-month program designed to soothe and strengthen sensitive skin."
    )
    duration = models.CharField(max_length=50, default="1 month")

    def __str__(self):
        return self.name


class NormalSkinProgram(models.Model):
    name = models.CharField(max_length=255, default="Daily Skin Maintenance Routine")
    description = models.TextField(
        default="A 2-week program for maintaining the health and radiance of normal skin."
    )
    duration = models.CharField(max_length=50, default="2 weeks")

    def __str__(self):
        return self.name
