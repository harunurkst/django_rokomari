from product.models import Category


def menus(request):
    categories = Category.objects.all()
    data = {
        'menus': categories
    }
    return data