from django.urls import path
from .views import writer_list, WriterListView, WriterDetailView

urlpatterns = [
    path('product/list', writer_list),
    path('writer/list', WriterListView.as_view()),
    path('writer/detail/<int:pk>', WriterDetailView.as_view(), name='writer_detail'),
]