from django.urls import path
from . import views

urlpatterns = [
    path('<day>/', views.get_day),
]