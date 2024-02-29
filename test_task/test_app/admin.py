from django.contrib import admin
from .models import *

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')


admin.site.register(Item, ItemAdmin)
