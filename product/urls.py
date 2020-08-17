from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.ItemDetailView.as_view(), name='item-detail')
]