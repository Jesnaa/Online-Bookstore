from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,Category,Payment, OrderPlaced,eBooks,BookTypes
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Cart,Whishlist
from django.contrib import messages
from logapp.models import User
from django.conf import settings
import razorpay

# from importlib.metadata import files
# # from settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
# # Create your views here.

def index(request):
    tblBook = Book.objects.all()
    category = Category.objects.all()
    cart = Cart.objects.all()
    return render(request,'index.html',{'datas':tblBook,'category':category,'cart':cart})
def ebook(request):
 return render(request,'E-Book.html')

def audiobooks(request):
     category = Category.objects.all()
     book = eBooks.objects.all()
     cart = Cart.objects.all()
     return render(request,'audiobooks.html',{'datas':book,'category':category,'cart':cart})
def ebooks(request):
    category = Category.objects.all()
    book = eBooks.objects.all()
    cart = Cart.objects.all()
    return render(request, 'audiobooks.html', {'datas': book, 'category': category, 'cart': cart})

def audiobook(request,id):
    rproduct = eBooks.objects.all()
    single = eBooks.objects.filter(book_id=id)
    cart = Cart.objects.all()
    category = Category.objects.all()
    return render(request, 'audiobook.html', {'result': single,'products':rproduct,'category':category,'cart':cart})

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
    category = Category.objects.all()
    books = Book.objects.all()
    if( Category.objects.filter(category_id=id)):
         book = Book.objects.filter(book_category_id=id)
    return render(request,'categorys.html',{'datas':book,'category':category,'books':books})
# def pricefilter(request,id):
#     category = Category.objects.all()
#     books = Book.objects.all()
#     if (Category.objects.filter(cid=id)):
#         book = Book.objects.filter(book_category_id=id)
#     return render(request, 'prize.html', {'datas': book, 'category': category, 'books': books})

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
     book = Book.objects.all()
     cart = Cart.objects.all()
     return render(request,'all product.html',{'datas':book,'category':category,'cart':cart})

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
                  messages.success(request, 'Book added to the Cart ')
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
            messages.success(request, 'Book added to the wishlist ')
            return redirect('allproduct')
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
    razoramount = total * 100
    print(razoramount)
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))

    data = {
        "amount": total,
        "currency": "INR",
        "receipt": "order_rcptid_11"

    }
    payment_response = client.order.create(data=data)
    print(payment_response)
    # {'id': 'order_Ki9yWEa6goK1si', 'entity': 'order', 'amount': 419, 'amount_paid': 0, 'amount_due': 419,
    #  'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created ', 'attempts': 0, 'notes': [],'created_at': 1668918227}
    order_id = payment_response['id']
    request.session['order_id'] = order_id
    order_status = payment_response['status']
    if order_status == 'created':
        payment = Payment(user=request.user,
                          amount=total,
                          razorpay_order_id=order_id,
                          razorpay_payment_status=order_status)
        payment.save()

    # context = {
    #     'razoramount': razoramount,
    #     'customer': customer,
    #     'total': total,
    #     'quantity': quantity,
    #     'cart_items': cart_items,
    #     'tax': tax,
    #     'grand_total': grand_total
    # }

    return render(request, 'checkout.html', {'datas': tblBook, 'category': category, 'product': cart, 'total':total,'razoramount':razoramount})

def payment_done(request):
    order_id=request.session['order_id']
    payment_id = request.GET.get('payment_id')
    print(payment_id)

    payment=Payment.objects.get(razorpay_order_id = order_id)

    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    # customer=Address_Book.objects.get(user=request.user,status=True)

    cart=Cart.objects.filter(user=request.user)
    # item = Product.objects.get(product=product, id=item_id)

    for c in cart:
        OrderPlaced(user=request.user,product=c.product,quantity=c.product_qty,payment=payment,is_ordered=True).save()
        c.delete()
    messages.success(request, 'Payment done successfully you can view the order details on your profile'
                              'Continue Shopping')
    return redirect('orders')



def dboyindex(request):
    return render(request,'dboyindex.html')
def dboyblank(request):
    return render(request,'dboyblank.html')
def dboy1(request):
    orders = OrderPlaced.objects.all()
    context = {
        'orders': orders,
    }
    return render(request,'dboy1.html',context)
def dboy2(request,id):
    orders = OrderPlaced.objects.filter(id=id)
    context = {
        'orders': orders,
    }
    return render(request,'dboy2.html',context)
def dboysetting(request):
    return render(request,'dboysetting.html')
# @login_required(login_url='login')
# def orders(request):
#     orders = OrderPlaced.objects.filter(
#         user=request.user, is_ordered=True).order_by('ordered_date')
#     context = {
#         'orders': orders,
#     }
#     return render(request, 'orders.html', context)
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
import os
import tempfile
import PyPDF2
import pyttsx3
from django.shortcuts import render
def pdf_to_audio(request):
    # if request.method == 'POST':
    #     pdf_file = request.FILES.get('pdf_file')
        pdf = eBooks.objects.get(book_id=id)
        pdf_file =pdf.book_pdf
        if pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                engine.save_to_file(text, temp_file.name)
                temp_file.flush()
                os.fsync(temp_file.fileno())
                audio_filename = temp_file.name
            return render(request, 'pdf_to_audio.html', {'audio_files': [audio_filename]})
    # else:
    #     return render(request, 'pdf_to_audio.html')
    # return HttpResponse()

import nltk
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
# sentiment_score = analyzer.polarity_scores(text)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
@method_decorator(csrf_exempt, name='dispatch')
class TextSummarizerView(View):
    template_name = 'summary.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        input_text = request.POST.get('input_text', '')
        num_sentences = int(request.POST.get('num_sentences', 5))
        sentences = nltk.sent_tokenize(input_text)
        words = [nltk.word_tokenize(sentence) for sentence in sentences]
        words = [[word for word in sentence if word.isalnum()] for sentence in words]
        summaries = []
        for i in range(len(sentences)):
            score = nltk.sentiment.vader.SentimentIntensityAnalyzer().polarity_scores(sentences[i])['compound']
            summaries.append((sentences[i], score))
        summaries = sorted(summaries, key=lambda x: x[1], reverse=True)
        summaries = [summary[0] for summary in summaries[:num_sentences]]
        summary_text = ' '.join(summaries)
        return render(request, self.template_name, {'input_text': input_text, 'summary_text': summary_text, 'num_sentences': num_sentences})