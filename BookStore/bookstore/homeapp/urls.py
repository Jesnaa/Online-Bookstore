from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
     path('product/<int:id>/',views.product,name='product'),
    # path('category/<slug:category_slug>',views.category, name='category'),
    path('checkout/',views.checkout,name='checkout'),
    # path('checkoutDetails/', views.checkoutDetails, name='checkoutDetails'),
     # path('wishlist/',views.wishlist,name='wishlist'),
path('add_wishlist/<int:id>/',views.add_wishlist,name='add_wishlist'),
  path('view_wishlist',views.view_wishlist,name='view_wishlist'),
  path('de_wishlist/<int:id>/',views.de_wishlist,name='de_wishlist'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('base/<int:id>/', views.base, name='base'),
    path('categorys/<int:id>/', views.categorys, name='categorys'),
    path('searchbar/', views.searchbar, name='searchbar'),
    # path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('addcart/<int:id>/', views.addcart, name='addcart'),
    path('de_cart/<int:id>/', views.de_cart, name='de_cart'),
    path('plusqty/<int:id>/',views.plusqty,name='plusqty'),
    path('minusqty/<int:id>/',views.minusqty,name='minusqty')
]
