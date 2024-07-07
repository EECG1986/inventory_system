from rest_framework import serializers
from .models import Supplier, Product, Order

class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Supplier.
    """
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Product.
    """
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Order.
    """
    class Meta:
        model = Order
        fields = '__all__'