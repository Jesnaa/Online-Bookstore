from django.urls import path
from . import views
from .views import TextSummarizerView

urlpatterns = [
     path('',views.index,name='index'),
     path('product/<int:id>/',views.product,name='product'),
     path('reviewss/<int:id>/', views.reviewss, name='reviewss'),
    # path('category/<slug:category_slug>',views.category, name='category'),
     path('checkout/',views.checkout,name='checkout'),
     path('ebook/',views.ebook,name='ebook'),
     path('pdf_to_audio/<int:id>/',views.pdf_to_audio,name='pdf_to_audio'),
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
    path('billview/', views.billview, name='billview'),
    path('text_summarizer/', TextSummarizerView.as_view(), name='text_summarizer'),
    path('dboyindex/', views.dboyindex, name='dboyindex'),
    path('dboyblank/', views.dboyblank, name='dboyblank'),
    path('dboy1/', views.dboy1, name='dboy1'),
    path('dboy3/', views.dboy3, name='dboy3'),
    path('dboy2/<int:id>/', views.dboy2, name='dboy2'),
    path('dboysetting/', views.dboysetting, name='dboysetting'),

    path('admin_index/', views.admin_index, name='admin_index'),
    path('admin_base/', views.admin_base, name='admin_base'),
    path('admin_delboy/', views.admin_delboy, name='admin_delboy'),
    path('add_deliveryboy/', views.add_deliveryboy, name='add_deliveryboy'),
    path('delete_dboy/<int:id>/', views.delete_dboy, name='delete_dboy'),
    path('admin_users/', views.admin_users, name='admin_users'),
    path('admin_uprofile/<int:id>/', views.admin_uprofile, name='admin_uprofile'),
    path('admin_dprofile/<int:id>/', views.admin_dprofile, name='admin_dprofile'),
    path('admin_category/', views.admin_category, name='admin_category'),
    path('addcat/', views.addcat, name='addcat'),
    path('deletecat/<int:id>/', views.deletecat, name='deletecat'),
    path('editcat/<int:id>/', views.editcat, name='editcat'),
    path('admin_ebook/', views.admin_ebook, name='admin_ebook'),
    path('add_ebook/', views.add_ebook, name='add_ebook'),
    path('admin_ebookview/<int:id>/', views.admin_ebookview, name='admin_ebookview'),
    path('deleteebook/<int:id>/', views.deleteebook, name='deleteebook'),
    path('ebookupdate/<int:id>/', views.ebookupdate, name='ebookupdate'),
    path('admin_book/', views.admin_book, name='admin_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('admin_bookview/<int:id>/', views.admin_bookview, name='admin_bookview'),
    path('deletebook/<int:id>/', views.deletebook, name='deletebook'),
    path('bookupdate/<int:id>/', views.bookupdate, name='bookupdate'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('order_detailslog/', views.order_detailslog, name='order_detailslog'),
    path('book_export/', views.book_export, name='book_export'),
    path('admin_reviews/', views.admin_reviews, name='admin_reviews'),


    path('pdf/<int:id>/', views.get,name='pdf'),
    path('run/', views.run, name='run'),
    # path('pause/', views.pause, name='pause'),
    # path('resume/<int:id>/', views.resume, name='resume'),
    path('stop/', views.stop, name='stop'),
    # path('order-delivered/<int:id>/',views.order_delivered, name='order-delivered'),
    path('translation/', views.translation, name='translation'),
    path('book_recommendations/', views.book_recommendations, name='book_recommendations'),
    path('rating_analysis/', views.rating_analysis, name='rating_analysis'),
    path('review_analysis/', views.review_analysis, name='review_analysis'),
    # path('generate_chart/', views.generate_chart, name='generate_chart'),
    path('send_order_confirmation_email/', views.send_order_confirmation_email, name='send_order_confirmation_email'),

]
