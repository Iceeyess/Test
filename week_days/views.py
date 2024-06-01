from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

d_dict = {
    'monday': 'В ПОНЕДЕЛЬНИК Черепаха Ткань купила на рубаху. ВТОРНИК - резала, кроила. В СРЕДУ шила, шила, шила…',
    'tuesday': 'ВТОРНИК следует за братом У него идей богато, Он за все берется смело И работа закипела.',
    'wednesday': 'Вот и средняя сестрица Не пристало ей лениться, А зовут её СРЕДА, Мастерица хоть куда.',
    'thursday': 'Брат ЧЕТВЕРГ и так и сяк, Он мечтательный чудак Повернул к концу недели И тянулся еле еле.',
    'friday': 'ПЯТНИЦА — сестра сумела Побыстрей закончить закончить дело. Если делаешь успехи, Время есть и для потехи.',
    'saturday': 'Предпоследний брат СУББОТА Не выходит на работу. Шалопай и озорник Он работать не привык.',
    'sunday': 'В гости ходит ВОСКРЕСЕНЬЕ, Очень любит угощение. Это самый младший брат, К Вам зайти он будет рад.'
}


def get_day(request: str, day: str) -> HttpResponse:
    return HttpResponse(d_dict.get(day, 'День не определен!'))


def get_day_by_numbers(request: str, day: int) -> HttpResponse:
    day_list = list(d_dict.keys())
    try:
        result = day_list[day - 1]
    except IndexError:
        return HttpResponseNotFound(f"Неверный номер дня - {day}")
    else:
        return HttpResponse(f"Сегодня {day} день недели")

