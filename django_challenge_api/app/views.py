from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Product
from app.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def retrieve(self, request, pk,  *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)
