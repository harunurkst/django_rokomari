from django.shortcuts import render
from django.views.generic import View
from .models import Item


class HomeView(View):
    def get(self, request):
        new_product = Item.objects.all().order_by('-pk')[:10]
        context = {
            'new_product': new_product
        }
        return render(request, 'index.html', context)

    def post(self, request):
        book = request.POST.get('book')
        print(book)
        return render(request, 'index.html')
