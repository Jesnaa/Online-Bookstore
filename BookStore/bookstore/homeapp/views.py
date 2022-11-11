from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Cart
from logapp.models import User
# Create your views here.
def index(request):
    tblBook = Book.objects.all()
    category = Category.objects.all()
    cart = Cart.objects.all()
    return render(request,'index.html',{'datas':tblBook,'category':category,'cart':cart})



def product(request,book_slug):
    rproduct = Book.objects.all()
    single = Book.objects.get(slug=book_slug)
    cart = Cart.objects.all()
    category = Category.objects.all()
    return render(request, 'product.html', {'result': single,'products':rproduct,'category':category,'cart':cart})


def checkout(request):
    category = Category.objects.all()
    tblBook = Book.objects.all()
    cart = Cart.objects.all()
    return render(request,'checkout.html',{'datas':tblBook,'category':category,'cart':cart})
def categorys(request):
    return render(request,'categorys.html')
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
def base(request):
    category = Category.objects.all()
    cart = Cart.objects.all()
    return render(request,'base1.html',{'category':category,'cart':cart})


def searchbar(request):
    category = Category.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Book.objects.filter(book_name__icontains=query)
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
                  return redirect(cart)
            else:
                  product_qty=1
                  price=item.book_price * product_qty

                  new_cart=Cart(user_id=user.id,product_id=item.book_id,product_qty=product_qty,price=price)
                  new_cart.save()
                  return redirect(cart)



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
    total=0
    for i in cart:
        total += i.product.book_price * i.product_qty
    category=Category.objects.all()
    # subcategory=Subcategory.objects.all()
    return render(request,'cart.html',{'cart':cart,'total':total,'category':category})

# Remove Items From Cart
def de_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)