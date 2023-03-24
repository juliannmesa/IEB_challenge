from dataclasses import fields
from rest_framework import serializers
from .models import Product
 
# create a serializer
class ProductSerializer(serializers.Serializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Product
        fields = ('id', 'name', 'sell_price', 'buy_price',  'description')