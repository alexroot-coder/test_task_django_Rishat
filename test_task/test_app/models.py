from django.db import models
from django.urls import reverse
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('items', kwargs={'item_id': self.pk})

    def get_display_price(self):
        return self.price / 100

    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'
