from django.urls import path
from . import views

urlpatterns = [
    path('team/<str:name>', views.index),
]
