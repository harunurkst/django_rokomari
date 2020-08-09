from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from product.models import Writer
from product.forms import WriterForm


class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


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


# class WriterCreateView(FormView):
#     form_class = WriterForm
#     template_name = 'dashboard/writer_form.html'
#
#     def form_valid(self, form):
#         form.save()
#         return redirect('writer-list')


class WriterCreateView(CreateView):
    model = Writer
    form_class = WriterForm
    template_name = 'dashboard/writer_form.html'


class WriterEditView(UpdateView):
    model = Writer
    fields = '__all__'
    template_name = 'dashboard/writer_form.html'


class WriterDeleteView(DeleteView):
    model = Writer
    success_url = reverse_lazy('writer-list')
    template_name = 'dashboard/writer_confirm_delete.html'






