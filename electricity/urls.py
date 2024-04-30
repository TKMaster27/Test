from django.urls import path
from .views import ChartData, home

urlpatterns = [
    path('', home, name='home'),
    path('api/chart/data', ChartData.as_view()),
]