from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('item/<int:item_id>/', items, name='items'),
    path('buy/<int:item_id>/', buy, name='buy')
]
