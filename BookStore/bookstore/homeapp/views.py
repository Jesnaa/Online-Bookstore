from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Category
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    tblBook = Book.objects.all()
    category = Category.objects.all()

    return render(request,'index.html',{'datas':tblBook,'category':category})



def product(request,book_slug):
    rproduct = Book.objects.all()
    single = Book.objects.get(slug=book_slug)

    category = Category.objects.all()
    return render(request, 'product.html', {'result': single,'products':rproduct,'category':category})


def checkout(request):
    return render(request,'checkout.html')
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
     if 'q' in request.GET:
         q = request.GET['q']

         multiple_q = Q(Q(book_name__icontains=q)| Q(book_author__icontains=q))
         tblBook = Book.objects.filter(multiple_q)

     else:
        tblBook = Book.objects.all()
        category = Category.objects.all()
     return render(request,'all product.html',{'datas':tblBook,'category':category})
# def allproduct(request):
#     tblBook = Book.objects.all()
#     category = Category.objects.all()
#     return render(request,'all product.html',{'datas':tblBook,'category':category})
def base(request):
    category = Category.objects.all()
    return render(request,'base1.html',{'category':category})


# def searchbar(request):
#     category = Category.objects.all()
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             products = Book.objects.filter(book_name__icontains=query)
#             return render(request, 'searchbar.html', {'datas':products,'category':category})
#         else:
#             print("No information to show")
#     return render(request, 'searchbar.html', {})
def searchbar(request):
    category = Category.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(book_name__icontains=query) | Q(book_author__icontains=query))
            products = Book.objects.filter(multiple_q)
            return render(request, 'searchbar.html', {'datas':products,'category':category})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {})