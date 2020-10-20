from django import template
from product.models import CartItem, Item

register = template.Library()


@register.simple_tag
def my_cart_items(username):
    print("username", username)
    items = CartItem.objects.filter(cart__user__username=username, cart__is_active=True)
    return {'items': items, 'count': items.count()}


@register.inclusion_tag(filename='product/related_product.html')
def related_items(category, count=4):
    print("category: ", category)
    items = Item.objects.filter(category=category)[:count]
    return {'item_list': items}
