from django.urls import path
from .views import get_sign_zodiac, get_test, get_sign_zodiac_with_numbers

urlpatterns = [
    path('test/', get_test),
    path('<int:sign_zodiac>/', get_sign_zodiac_with_numbers, name='horoscope-name'),
    path('<str:sign_zodiac>/', get_sign_zodiac),
]
