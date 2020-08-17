from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import Item
from .forms import AddToCartForm


class HomeView(View):
    def get(self, request):
        new_product = Item.objects.new_items()
        top_product = Item.objects.top_items()
        context = {
            'new_product': new_product,
            'top_product': top_product
        }
        return render(request, 'index.html', context)

    def post(self, request):
        book = request.POST.get('book')
        print(book)
        return render(request, 'index.html')


class ItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = super().get_object()
        print(object)
        context['form'] = AddToCartForm(instance=object)
        return context



