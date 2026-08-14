from django.urls import path 

from .views import * 

urlpatterns = [
    path('predict/', PredictSkinDiseaseView.as_view(), name='predict'),
    path('health/', HealthCheckView.as_view(), name='health'),
]