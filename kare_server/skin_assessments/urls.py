from django.urls import path
from .views import PredictSkinAPIView as predict_skin

urlpatterns = [
    path('predict/', predict_skin.as_view(), name='predict'),
]
