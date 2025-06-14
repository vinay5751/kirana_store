from django.shortcuts import render, redirect, get_object_or_404
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


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("inventory:product_list")
    else:
        form = ProductForm(instance=product)
    context = {"form": form, "product": product}
    return render(request, "inventory/edit_product.html", context)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("inventory:product_list")

    context = {"product": product}
    return render(request, "inventory/delete_confirm.html", context)
