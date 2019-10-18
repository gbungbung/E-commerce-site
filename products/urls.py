from django.urls import path
from products import views

app_name= 'products'
urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('product/<int:pk>-<slug:slug>/', views.ProductDetail.as_view(), name='product-detail'),
   # path('products/categorie/<slug:slug>/', views.CategoryView.as_view(), name='products'),
]

