from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('add-to-cart', views.AddToCartView.as_view(), name='add-to-cart'),
    path('checkout', views.Checkout.as_view(), name='checkout'),
]