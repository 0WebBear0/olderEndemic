from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('product/<int:product_id>/', views.productsDetail, name='product_detail'),
    path('category/<int:category_id>/', views.categoryDetail, name='category_detail'),
    path('firm/<int:firm_id>/', views.firmView, name='firm_view'),
    path('Catalog/', views.Catalog, name='Catalog'),
    path('Map/', views.Map, name='Map'),
]
