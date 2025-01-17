from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_create_view, name="product_create"),
    path("<int:pk>/", views.product_detail_view, name="product_detail"),
]
