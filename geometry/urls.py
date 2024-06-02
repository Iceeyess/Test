from django.urls import path
from .views import get_rectangle_area, get_square_area, get_circle_area, get_redirect_rectangle_area, \
    get_redirect_square_area, get_redirect_circle_area

urlpatterns = [
    path('rectangle/<int:length>/<int:width>/', get_rectangle_area),
    path('get_rectangle_area/<int:length>/<int:width>/', get_redirect_rectangle_area),
    path('square/<int:length>/', get_square_area),
    path('get_square_area/<int:length>/', get_redirect_square_area),
    path('circle/<int:radius>/', get_circle_area),
    path('get_circle_area/<int:radius>/', get_redirect_circle_area),
]
