from django.shortcuts import render

from catalog.models import Products


def index(request):
    product_list = Products.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, телефон: {phone}, сообщение: {message}.')

    return render(request, 'catalog/contacts.html')


def catalog(request):
    product_list = Products.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/catalog.html', context)


def product(request, pk):
    context = {
        'object': Products.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)
