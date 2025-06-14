from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.db.models import F, Sum


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


def dashboard(request):
    total_products = Product.objects.count()
    total_stock_value = (
        Product.objects.aggregate(total_value=Sum(F("cost_price") * F("quantity")))[
            "total_value"
        ]
        or 0.00
    )

    low_stock_products = Product.objects.filter(quantity__lt=5)
    context = {
        "total_products": total_products,
        "total_stock_value": total_stock_value,
        "low_stock_products": low_stock_products,
    }
    return render(request, "inventory/dashboard.html", context)
