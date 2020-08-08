from django.shortcuts import render
from django.views.generic import ListView, DetailView
from product.models import Writer


def writer_list(request):
    writers = Writer.objects.all()
    return render(request, 'dashboard/writer_list.html', {'writers': writers})


class WriterListView(ListView):
    model = Writer
    template_name = 'dashboard/writer_list.html'
    context_object_name = 'writers'


class WriterDetailView(DetailView):
    model = Writer
    template_name = 'dashboard/writer_detail.html'
    context_object_name = 'writer'


