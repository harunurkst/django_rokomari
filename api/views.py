from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from product.models import CartItem
from rest_framework.response import Response


class RemoveFromCartView(APIView):
    def get(self, request, cart_item_id):
        print("in view")
        item = get_object_or_404(CartItem, pk=cart_item_id)
        item.delete()
        print("deleted")
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



