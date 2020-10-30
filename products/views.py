from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render


# Create your views here.
from products.models import Product


def home_view(request, *args, **kwargs):
    context = {"name": "Amandine"}
    return render(request, "home.html", context)


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404 # render html page, with HTTP status code of 404
    # return HttpResponse(f"Product id {obj.id}")
    return render(request, "products/detail.html", {"object": obj})


def product_list_view(request, *args, **kwargs):
    try:
        objects = Product.objects.all()
        context = {"object_list": objects}
    except Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id {obj.id}")
    return render(request, "products/list.html", context)


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"}) # return JSON with HTTP status code of 404
    return JsonResponse({"id": obj.id})

