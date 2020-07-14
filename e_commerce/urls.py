from django.urls import path
from . import views
from e_commerce.views import product_detail

urlpatterns = [
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('', views.index, name='index'),
]