from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render


# Create your views here.
from products.models import Product


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404 # render html page, with HTTP status code of 404
    return HttpResponse(f"Product id {obj.id}")


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with HTTP status code of 404
    return JsonResponse({"id": obj.id})

