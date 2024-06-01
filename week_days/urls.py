from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.get_day_by_numbers),
    path('<str:day>/', views.get_day),
]
