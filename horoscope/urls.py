from django.urls import path
from .views import get_sign_zodiac, get_test

urlpatterns = [
    path('test/', get_test),
    path('<sign_zodiac>/', get_sign_zodiac),

]
