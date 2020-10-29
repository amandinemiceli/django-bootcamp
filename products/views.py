from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from products.models import Product


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return HttpResponse(f"Product id {obj.id}")


def product_api_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return JsonResponse({"id": obj.id})

