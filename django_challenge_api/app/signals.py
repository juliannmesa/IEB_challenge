from django.dispatch import receiver
from django.db.models.signals import (
	pre_save,
	post_save,
)
from app.models import Product, HistoricPrice

@receiver(pre_save, sender=Product)
def validate_price_change(instance, **kwargs):
	print('adads')
	if instance.id:
		old_instance = Product.objects.get(id=instance.id)
		if old_instance.sell_price != instance.sell_price or old_instance.buy_price != instance.buy_price:
			setattr(
				instance,
				'historic_prices',
				{
					'sell_price': old_instance.sell_price,
					'buy_price': old_instance.buy_price
				}
			)



@receiver(post_save, sender=Product)
def create_or_update_historic_price(instance, created, **kwargs):
	if created:
		HistoricPrice.objects.create(product=instance, sell_price=instance.sell_price, buy_price=instance.buy_price)
	else:
		if hasattr(instance, 'historic_prices'):
			HistoricPrice.objects.create(
				product=instance,
				sell_price=instance.historic_prices.get('sell_price'),
				buy_price=instance.historic_prices.get('buy_price')
			)