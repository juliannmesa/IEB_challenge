import uuid

from django.db import models

class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Product(BaseModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	sell_price = models.FloatField()
	buy_price = models.FloatField()
	description = models.TextField()

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.name


class HistoricPrice(BaseModel):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
	sell_price = models.FloatField()
	buy_price = models.FloatField()

	class Meta:
		verbose_name = 'HistoricPrice'
		verbose_name_plural = 'HistoricPrices'

	def __str__(self):
		return f'({self.product.name}), [{self.created_at}]'


