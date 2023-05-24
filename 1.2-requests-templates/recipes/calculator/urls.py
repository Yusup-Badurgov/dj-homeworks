
from django.urls import path
from calculator.views import recipes_cal

urlpatterns = [
    path('<str:recipe>/', recipes_cal)
]