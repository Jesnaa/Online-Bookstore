from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Cart,Whishlist
from django.contrib import messages
from logapp.models import User
# Create your views here.
def index(request):
    tblBook = Book.objects.all()
    category = Category.objects.all()
    cart = Cart.objects.all()
    return render(request,'index.html',{'datas':tblBook,'category':category,'cart':cart})


def product(request,id):
    rproduct = Book.objects.all()
    single = Book.objects.filter(book_id=id)
    cart = Cart.objects.all()
    category = Category.objects.all()
    return render(request, 'product.html', {'result': single,'products':rproduct,'category':category,'cart':cart})


# def product(request,book_slug):
#     rproduct = Book.objects.all()
#     single = Book.objects.get(slug=book_slug)
#     cart = Cart.objects.all()
#     category = Category.objects.all()
#     return render(request, 'product.html', {'result': single,'products':rproduct,'category':category,'cart':cart})
#


def categorys(request,id):
    if( Category.objects.filter(category_id=id)):
         tblBook = Book.objects.filter(book_category_id=id)
    return render(request,'categorys.html',{'datas':tblBook,})

# def category(request,category_slug):
#     catslug = Category.objects.get(slug=category_slug)
#     return render(request, 'categorys.html', {'catgry': catslug})
# def category(request):
#     if request.method == 'GET':
#         category_id = int(request.GET.get('category_id', default=1))
#         current_category = Category.objects.get(pk=category_id)
#         products = current_category.products.all()
#     return render(request, 'categorys.html',{'products': products})

def allproduct(request):
     category = Category.objects.all()
     tblBook = Book.objects.all()
     cart = Cart.objects.all()
     return render(request,'all product.html',{'datas':tblBook,'category':category,'cart':cart})

# def allproduct(request):
#     tblBook = Book.objects.all()
#     category = Category.objects.all()
#     return render(request,'all product.html',{'datas':tblBook,'category':category})
def base(request,id):
    tblBook = Book.objects.all()
    category = Category.objects.filter(category_id=id)
    cart = Cart.objects.all()
    return render(request,'base1.html',{'datas':tblBook,'category':category,'cart':cart})


def searchbar(request):
    category = Category.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(book_name__icontains=query) | Q(book_author__icontains=query))
            products = Book.objects.filter(multiple_q)
            return render(request, 'searchbar.html', {'datas':products,'category':category})
        else:
            print("No information to show")
    return render(request, 'searchbar.html', {})


@login_required(login_url='login')
def addcart(request,id):
      user = request.user
      item=Book.objects.get(book_id=id)
      if item.book_quantity>0:
            if Cart.objects.filter(user_id=user,product_id=item).exists():
                  messages.success(request, 'Book Already in the cart ')
                  return redirect(allproduct)
            else:
                  product_qty=1
                  price=item.book_price * product_qty

                  new_cart=Cart(user_id=user.id,product_id=item.book_id,product_qty=product_qty,price=price)
                  new_cart.save()
                  return redirect(allproduct)



# Cart Quentity Plus Settings
def plusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product.book_quantity > cart.product_qty:
            cart.product_qty +=1
            cart.price=cart.product_qty * cart.product.book_price
            cart.save()
            return redirect('cart')
        # messages.success(request, 'Out of Stock')
        return redirect('cart')

# Cart Quentity minus Settings
def minusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product_qty > 1 :
            cart.product_qty -=1
            cart.price=cart.product_qty * cart.product.book_price
            cart.save()
            return redirect('cart')
        return redirect('cart')



# View Cart Page
@login_required(login_url='login')
def cart(request):
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    totalitem=0
    total=0
    for i in cart:
        total += i.product.book_price * i.product_qty
        totalitem = len(cart)

    category=Category.objects.all()
    # subcategory=Subcategory.objects.all()
    return render(request,'cart.html',{'cart':cart,'total':total,'category':category,'totalitem':totalitem})

# Remove Items From Cart
def de_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)

# add to wishlist
@login_required(login_url='login')
def add_wishlist(request,id):
    user = request.user
    item=Book.objects.get(book_id=id)
    if Whishlist.objects.filter( user_id =user,product_id=item).exists():
        messages.success(request, 'Book Already in the wishlist ')
        return redirect('allproduct')
    else:
            new_wishlist=Whishlist(user_id=user.id,product_id=item.book_id)
            new_wishlist.save()
            return redirect('view_wishlist')
    # messages.success(request, 'Sign in..!!')
    # return redirect(index)


#Wishlist View page
@login_required(login_url='login')
def view_wishlist(request):
        user = request.user
        wish=Whishlist.objects.filter(user_id=user)
        category=Category.objects.all()

        return render(request,"wishlist.html",{'wishlist':wish,'category':category})


# Remove Items From Wishlist
def de_wishlist(request,id):
    Whishlist.objects.get(id=id).delete()
    return redirect('view_wishlist')


def checkout(request):
    user = request.user
    product = Cart.objects.filter(user_id=user)
    total = 0
    for i in product:
        total += i.product.book_price * i.product_qty
        cart = Cart.objects.filter(user_id=user)
    category = Category.objects.all()
    tblBook = Book.objects.all()

    return render(request, 'checkout.html', {'datas': tblBook, 'category': category, 'product': cart, 'total':total})
#
# def checkoutDetails(request):
#     if request.method == "POST":
#
#         last_name = request.POST.get('last_name')
#         first_name = request.POST.get('first_name')
#         email = request.POST.get('email')
#         phonenumber = request.POST.get('phonenumber')
#         user_id = request.user.id
#         username = request.POST.get('username')
#         hname = request.POST.get('hname')
#         country = request.POST.get('country')
#         state = request.POST.get('state')
#         city = request.POST.get('city')
#         pincode = request.POST.get('pincode')
#
#         user = User.objects.get(id=user_id)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.phonenumber = phonenumber
#         user.email = email
#         user.city = city
#         user.country = country
#         user.state = state
#         user.pincode = pincode
#         user.username = username
#         user.hname = hname
#
#         user.save()
#         return redirect('checkout')
