from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
    products = Product.objects.all().order_by("name")

    context = {"products": products}

    return render(request, "inventory/product_list.html", context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventory:product_list")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "inventory/add_product.html", context)
