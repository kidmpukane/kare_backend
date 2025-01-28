from django.contrib import admin
from .programs import (
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
