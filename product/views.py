from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Item, Cart, CartItem
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


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request):
        qty = request.GET.get("qty", 1)
        item_id = request.GET.get("item_id")
        item = Item.objects.get(pk=item_id)

        cart_obj, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        CartItem.objects.create(item=item, quantity=qty, cart=cart_obj)
        messages.success(request, 'Item added to your cart')
        return redirect('home')


class Checkout(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.get(user=request.user, is_active=True)
        print(cart)
        context = {
            'cart': cart
        }
        return render(request, 'product/checkout.html', context)

