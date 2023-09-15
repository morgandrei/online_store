from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Products, Contacts


def index(request):
    product_list = Products.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/index.html', context)


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        context_data['object_list'] = Contacts.objects.all()
        return context_data


class CatalogListView(ListView):
    model = Products


class ProductsDetailView(DetailView):
    model = Products

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        #context_data = super().get_context_data(*args, **kwargs)
        #product_item = Products.objects.get(pk=self.kwargs.get('pk'))
        context_data = {
            'object': Products.objects.get(pk=self.kwargs.get('pk'))
        }

        return context_data
