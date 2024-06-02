from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

def get_test(request):
    return render(request, 'index.html')


def get_sign_zodiac(request, sign_zodiac: str):
    zodiac_answer = zodiac_dict.get(sign_zodiac)
    if zodiac_answer:
        return HttpResponse(f"{zodiac_answer}")
    return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")


def get_sign_zodiac_with_numbers(request, sign_zodiac: int):
    if 0 <= sign_zodiac <= len(list(zodiac_dict)):
        zodiac_names = list(zodiac_dict)
        zodiac_name = zodiac_names[sign_zodiac - 1]
        redirect_url = reverse('horoscope-name', args=(zodiac_name, ))
        # return redirect(f"/horoscope/{zodiac_name}/", permanent=True)
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_zodiac}")

