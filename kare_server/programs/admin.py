from django.contrib import admin
from .models import (
    DrySkinProgram,
    OilySkinProgram,
    CombinationSkinProgram,
    SensitiveSkinProgram,
    NormalSkinProgram,
)

admin.site.register(DrySkinProgram)
admin.site.register(OilySkinProgram)
admin.site.register(CombinationSkinProgram)
admin.site.register(SensitiveSkinProgram)
admin.site.register(NormalSkinProgram)
