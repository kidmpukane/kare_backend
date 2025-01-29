from django.urls import path
from .views import PredictSkinAPIView as predict_skin, FetchAssessmentByUserIdView as fetch_assessment_by_user_id, FetchAllAssessmentsView as fetch_all_assessments

urlpatterns = [
    path('predict/', predict_skin.as_view(), name='predict'),
    path('fetch/<int:user_id>/', fetch_assessment_by_user_id.as_view(), name='fetch'),
    path('fetch-all/', fetch_all_assessments.as_view(), name='fetch_all'),
]
