from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_sign_zodiac(request, sign_zodiac):
    with open('/home/dima/PycharmProjects/DjangoArtem/my_page/horoscope/static/index.html') as f:
        file = f.read()
    return render(request, file)
    # if sign_zodiac == 'taurus':
    #     return HttpResponse(f"Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
    # elif sign_zodiac == 'aries':
    #     return HttpResponse(f"Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")
    # elif sign_zodiac == 'gemini':
    #     return HttpResponse(f"Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
    # else:
    #     return HttpResponse(f"Неизвестный знак зодиака - {sign_zodiac}")

