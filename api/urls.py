from django.urls import path
from . import views


urlpatterns = [
    path('remove-cart-item/<int:cart_item_id>', views.RemoveFromCartView.as_view(), name='remove-cart-item'),
]