from django.urls import path
from . import views
from .views import TextSummarizerView

urlpatterns = [
     path('',views.index,name='index'),
     path('product/<int:id>/',views.product,name='product'),
    # path('category/<slug:category_slug>',views.category, name='category'),
     path('checkout/',views.checkout,name='checkout'),
     path('ebook/',views.ebook,name='ebook'),

     path('ebooks/',views.ebooks,name='ebooks'),
     path('audiobook/<int:id>/',views.audiobook,name='audiobook'),
     path('audiobooks/', views.audiobooks, name='audiobooks'),
     path('paymentdone/', views.payment_done, name='paymentdone'),
     path('orders/', views.allproduct, name='orders'),
    # path('checkoutDetails/', views.checkoutDetails, name='checkoutDetails'),
     # path('wishlist/',views.wishlist,name='wishlist'),
    path('add_wishlist/<int:id>/',views.add_wishlist,name='add_wishlist'),
    path('view_wishlist',views.view_wishlist,name='view_wishlist'),
    path('de_wishlist/<int:id>/',views.de_wishlist,name='de_wishlist'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('base/<int:id>/', views.base, name='base'),
    path('categorys/<int:id>/', views.categorys, name='categorys'),
    # path('pricefilter/<int:id>/', views.pricefilter, name='pricefilter'),
    path('searchbar/', views.searchbar, name='searchbar'),
    # path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('addcart/<int:id>/', views.addcart, name='addcart'),
    path('de_cart/<int:id>/', views.de_cart, name='de_cart'),
    path('plusqty/<int:id>/',views.plusqty,name='plusqty'),
    path('minusqty/<int:id>/',views.minusqty,name='minusqty'),
    path('text_summarizer/', TextSummarizerView.as_view(), name='text_summarizer'),
    path('dboyindex/', views.dboyindex, name='dboyindex'),
    path('dboyblank/', views.dboyblank, name='dboyblank'),
    path('dboy1/', views.dboy1, name='dboy1'),
    path('dboy2/', views.dboy2, name='dboy2'),
    path('dboysetting/', views.dboysetting, name='dboysetting'),

]
