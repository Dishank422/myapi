from django.urls import path
from . import views

urlpatterns = [
    path('sport/<str:sport_name>', views.sport),
    path('sex/<str:s>', views.sex),
]
