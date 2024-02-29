import stripe
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def buy(request, item_id):
    YOUR_DOMAIN = "http://127.0.0.1:8000"
    item = Item.objects.get(id=item_id)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': item.price,
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    }
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN,
        cancel_url=YOUR_DOMAIN,
    )
    return JsonResponse({
        'id': checkout_session.id
    })


def index(request):
    data_items = Item.objects.all()
    return render(request, 'test_app/index.html', {'data_items': data_items})


def items(request, item_id):
    try:
        data_items = Item.objects.get(pk=item_id)
        return render(request, 'test_app/item.html', {'item_id': item_id,
                                                      'data_items': data_items,
                                                      'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})
    except ObjectDoesNotExist:
        raise Http404


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</>")
