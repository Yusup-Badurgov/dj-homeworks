from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')  # Забираю get параметр если он есть

    # Возвращаю  отсортированные данные согласно указанному в get параметре фильтру
    if sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('min_price')
    elif sort == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones # в контекст передается список объекта отсортированный согласно фильтру
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug) # получаю объект из базы данных по полю slug переданного в url
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
