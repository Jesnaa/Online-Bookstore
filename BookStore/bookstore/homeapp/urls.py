from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
     path('product/<slug:book_slug>',views.product,name='product'),
    # path('category/<slug:category_slug>',views.category, name='category'),
    path('',views.checkout,name='checkout'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('base/', views.base, name='base'),
    path('categorys/', views.categorys, name='categorys'),
  path('searchbar/', views.searchbar, name='searchbar'),
    # path('search/', views.search, name='search'),
]
