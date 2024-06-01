from django.urls import path
from .views import get_sign_zodiac, get_test, get_sign_zodiac_with_numbers, get_sign_zodiac_with_16

urlpatterns = [
    path('test/', get_test),
    path('16/', get_sign_zodiac_with_16),
    path('<int:sign_zodiac>/', get_sign_zodiac_with_numbers),
    path('<str:sign_zodiac>/', get_sign_zodiac),
]
