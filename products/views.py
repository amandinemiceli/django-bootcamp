from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, redirect

from .forms import ProductModelForm
from products.models import Product


# Create your views here.
def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    context = {"name": "Amandine", "query": query}
    return render(request, "home.html", context)


# def product_create_view(request, *args, **kwargs):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 title_from_input = my_form.cleaned_data.get('title')
#                 Product.objects.create(title=title_from_input)
#     return render(request, "forms.html", {})


def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        obj = form.save(commit=False)
        # same as Product(**data)
        # do some stuff then
        obj.save()

        # other method to save in DB:
        # data = form.cleaned_data
        # Product.objects.create(**data)

        form = ProductModelForm()
        # return HttpResponseRedirect("/success")
        # return redirect("/success")
    return render(request, "forms.html", {"form": form})


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

