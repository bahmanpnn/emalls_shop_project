from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view.as_view(), name='product-list'),
    path('cat/<cat>', views.product_list_view.as_view(), name='product-categories-list'),
    path('brand/<brand>', views.product_list_view.as_view(), name='product-list-by-brand'),
    path('<slug:slug>', views.product_detail_view.as_view(), name='product-detail'),

]
