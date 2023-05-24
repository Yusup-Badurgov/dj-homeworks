import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_num = request.GET.get('page', 1)
    csv_file = settings.BUS_STATION_CSV

    with open(csv_file, encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data_list = []
        for row in reader:
            data_list.append(row)

    paginator = Paginator(data_list, 10)
    data_pagi = paginator.get_page(page_num)

    context = {
        'bus_stations': data_pagi,
        'page': data_pagi
    }
    return render(request, 'stations/index.html', context)
