from django.contrib import admin
from .models import (
    SkinProgram,
    CurrentProgram
)

admin.site.register(SkinProgram)
admin.site.register(CurrentProgram)

