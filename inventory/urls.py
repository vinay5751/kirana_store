from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path("products/", views.product_list, name="product_list"),
    path("add-product/", views.add_product, name="add_product"),
    path("product/<int:pk>/edit", views.edit_product, name="edit_product"),
]
