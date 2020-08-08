from django.shortcuts import render
from django.views.generic import View


def home(request):
    return render(request, 'index.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        book = request.POST.get('book')
        print(book)
        return render(request, 'index.html')
