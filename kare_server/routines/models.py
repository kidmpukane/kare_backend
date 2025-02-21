from django.db import models
from programs.models import SkinProgram


class SkinRoutine(models.Model):
    programs = models.ManyToManyField(
        SkinProgram, related_name="program_routines"
    )
    image = models.ImageField(upload_to="images/")
    routine_name = models.CharField(max_length=255, default="Morning Routine")
    description = models.CharField(
        max_length=255, default="Morning Routine Description"
    )
    start_date = models.TimeField(auto_now=False, auto_now_add=False)
    end_date = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.routine_name


class Instructions(models.Model):
    routines = models.ManyToManyField(
        SkinRoutine, related_name="routine_instructions"
    )
    image = models.ImageField(upload_to="images/")
    instruction_name = models.CharField(
        max_length=255, default="Instruction Name"
    )
    instruction_description = models.CharField(
        max_length=255, default="Instruction Description"
    )
    instruction_number = models.IntegerField(null=True)

    def __str__(self):
        return self.instruction_name
