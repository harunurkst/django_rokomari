from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from product.models import CartItem, Item, Category
from rest_framework.response import Response
from .serializers import ItemSerializer, CreateItemSerializer, CategorySerializer


class RemoveFromCartView(APIView):
    def get(self, request, cart_item_id):
        item = get_object_or_404(CartItem, pk=cart_item_id)
        item.delete()
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)


class SearchProductView(APIView):
    """
    response:
    [
        {
            "category": "",
            "product_name": "",
            "new_price": "",
            "old_price":
        },
    ]
    """
    def get(self, request):
        item_list = Item.objects.all()
        serializer = ItemSerializer(item_list, many=True)
        return Response(serializer.data)


class CreateProductView(APIView):
    def post(self, request):
        serializer = CreateItemSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            serializer.save()
            return Response({'status': 'ok'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCategoryAPI(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username="harun")
            return Response({'status': 'ok'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategoryApi(APIView):
    def post(self, request, cid):
        category = Category.objects.get(pk=cid)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


