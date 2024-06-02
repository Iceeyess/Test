from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from my_page.urls import GEOMETRY_ROOT
from django.urls import reverse


# Create your views here.
def get_rectangle_area(request, length, width) -> HttpResponse:
    return HttpResponse(f"Площадь прямоугольника размером {length}x{width} равна {length * width}")


def get_square_area(request, length) -> HttpResponse:
    return HttpResponse(f"Площадь квадрата размером {length}x{length} равна {length * length}")


def get_circle_area(request, radius) -> HttpResponse:
    return HttpResponse(f"Площадь круга радиуса {radius} равна {3.14 * radius ** 2}")


#  GEOMETRY_ROOT = 'calculate_geometry/'
def get_redirect_rectangle_area(request, length, width) -> HttpResponse:
    url_route = reverse('rectangle-url', args=(length, width))
    return HttpResponseRedirect(url_route)


def get_redirect_square_area(request, length) -> HttpResponse:
    url_route = reverse('square-url', args=(length, ))
    return HttpResponseRedirect(url_route)


def get_redirect_circle_area(request, radius) -> HttpResponse:
    url_route = reverse('circle-url', args=(radius, ))
    return HttpResponseRedirect(url_route)