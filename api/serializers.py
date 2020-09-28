from rest_framework import serializers
from product.models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ('name', 'new_price', 'old_price', 'category', 'featured_image')


class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'new_price', 'old_price', 'category', 'size', 'color', 'description')


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        name = validated_data["name"]
        category = Category.objects.create(name=name)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

