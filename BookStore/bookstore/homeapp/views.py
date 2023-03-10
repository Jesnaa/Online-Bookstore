from audioop import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book,Category,Payment, OrderPlaced,eBooks,BookTypes,ReviewRating
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Cart,Whishlist
from django.contrib import messages
from logapp.models import User
from django.conf import settings
import razorpay
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf

# from importlib.metadata import files
# # from settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
# # Create your views here.

def index(request):
    count = Cart.objects.filter(user=request.user.id).count()
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    tblBook = Book.objects.all()
    category = Category.objects.all()
    cart = Cart.objects.all()

    return render(request,'index.html',{'datas':tblBook,'category':category,'cart':cart,'count':count,'w_count':w_count})
def ebook(request):
 return render(request,'E-Book.html')

def audiobooks(request):
     w_count = Whishlist.objects.filter(user=request.user.id).count()
     count = Cart.objects.filter(user=request.user.id).count()
     category = Category.objects.all()
     book = eBooks.objects.all()
     cart = Cart.objects.all()
     return render(request,'audiobooks.html',{'datas':book,'category':category,'cart':cart,'count':count,'w_count':w_count})

def ebooks(request):
    category = Category.objects.all()
    book = eBooks.objects.all()
    cart = Cart.objects.all()
    return render(request, 'audiobooks.html', {'datas': book, 'category': category, 'cart': cart})

def audiobook(request,id):
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    count = Cart.objects.filter(user=request.user.id).count()
    rproduct = eBooks.objects.all()
    single = eBooks.objects.filter(book_id=id)
    cart = Cart.objects.all()
    category = Category.objects.all()
    return render(request, 'audiobook.html', {'result': single,'products':rproduct,'category':category,'cart':cart,'count':count,'w_count':w_count})

def product(request,id):
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    count = Cart.objects.filter(user=request.user.id).count()
    products = Book.objects.all()
    single = Book.objects.filter(book_id=id)
    cart = Cart.objects.all()
    category = Category.objects.all()
    orderproduct = OrderPlaced.objects.filter(user=request.user, is_ordered=True).exists()
    review = ReviewRating.objects.filter(product_id=id, status=True)
    book = get_object_or_404(Book, book_id=id)
    average_review = book.averageReview()
    context = {
        'book': book,
        'review_count': book.countReview(),
        'averageReview' : average_review
    }
    return render(request, 'product.html', {'context':context,'result': single,'products':products,'category':category,'cart':cart,'count':count,'w_count':w_count,'orderproduct':orderproduct,'review':review})


# def product(request,book_slug):
#     rproduct = Book.objects.all()
#     single = Book.objects.get(slug=book_slug)
#     cart = Cart.objects.all()
#     category = Category.objects.all()
#     return render(request, 'product.html', {'result': single,'products':rproduct,'category':category,'cart':cart})
#
def reviewss(request,id):
        if request.method == 'POST':
            try:
                reviews = ReviewRating.objects.get(user_id=request.user.id, product_id=id)
                headline = request.POST.get('headline')
                rating = request.POST.get('rating')
                review = request.POST.get('review')
                reviews.headline = headline
                reviews.rating = rating
                reviews.review = review
                reviews.save()
                messages.success(request, 'Thank you! Your review has been updated.')
                return redirect(request.META.get('HTTP_REFERER'))
            except ReviewRating.DoesNotExist:
                headline = request.POST.get('headline')
                rating = request.POST.get('rating')
                review = request.POST.get('review')
                data = ReviewRating()
                data.headline = headline
                data.rating = rating
                data.review = review
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = id
                data.user_id = request.user.id
                if OrderPlaced.objects.filter(user_id=request.user.id, product_id=id, is_ordered=True).exists():
                    data.save()
                    messages.success(request, 'Thank you! Your review has been submitted.')
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.warning(request, 'You can only review products that you have purchased.')
                    return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('/')


def categorys(request,id):
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    count = Cart.objects.filter(user=request.user.id).count()
    category = Category.objects.all()
    books = Book.objects.all()
    if( Category.objects.filter(category_id=id)):
         book = Book.objects.filter(book_category_id=id)
    return render(request,'categorys.html',{'datas':book,'category':category,'books':books,'count':count,'w_count':w_count})
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
     w_count = Whishlist.objects.filter(user=request.user.id).count()
     count = Cart.objects.filter(user=request.user.id).count()
     category = Category.objects.all()
     book = Book.objects.all()
     cart = Cart.objects.all()
     return render(request,'all product.html',{'datas':book,'category':category,'cart':cart,'count':count,'w_count':w_count})

# def allproduct(request):
#     tblBook = Book.objects.all()
#     category = Category.objects.all()
#     return render(request,'all product.html',{'datas':tblBook,'category':category})
def base(request,id):
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    count = Cart.objects.filter(user=request.user.id).count()
    tblBook = Book.objects.all()
    category = Category.objects.filter(category_id=id)
    cart = Cart.objects.all()
    return render(request,'base1.html',{'datas':tblBook,'category':category,'cart':cart,'count':count,'w_count':w_count})


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
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    count = Cart.objects.filter(user=request.user.id).count()
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    totalitem=0
    total=0
    for i in cart:
        total += i.product.book_price * i.product_qty
        totalitem = len(cart)

    category=Category.objects.all()
    # subcategory=Subcategory.objects.all()
    return render(request,'cart.html',{'cart':cart,'total':total,'category':category,'totalitem':totalitem,'count':count,'w_count':w_count})

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
        count = Cart.objects.filter(user=request.user.id).count()
        w_count = Whishlist.objects.filter(user=request.user.id).count()
        user = request.user
        wish=Whishlist.objects.filter(user_id=user)
        category=Category.objects.all()
        return render(request,"wishlist.html",{'wishlist':wish,'category':category,'w_count':w_count,'count':count})


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
        c.product.book_quantity -= c.product_qty
        c.product.save()
    # messages.success(request, 'Payment done successfully you can view the order details on your profile'
    #                           'Continue Shopping')
    return redirect('billview')

def billview(request):
    count = Cart.objects.filter(user=request.user.id).count()
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    orders = OrderPlaced.objects.filter(
        user=request.user, is_ordered=True).order_by('ordered_date')
    return render(request,'bill_view.html',{ 'orders': orders,'w_count':w_count,'count':count})


def dboyindex(request):
    return render(request,'dboyindex.html')
def dboyblank(request):
    return render(request,'dboyblank.html')
def dboy1(request):
    orders = OrderPlaced.objects.exclude(status='Delivered')
    context = {
        'orders': orders,
    }
    return render(request,'dboy1.html',context)
def dboy2(request,id):
    orders = OrderPlaced.objects.filter(id=id)
    context = {
        'orders': orders,
    }
    for order in orders:
       if order.status == 'Pending':
                 order.status = 'Delivered'
                 order.save()

    return render(request,'dboy2.html',context)

def dboysetting(request):
    return render(request,'dboysetting.html')




import os
import tempfile
from io import BytesIO

import PyPDF2
import pyttsx3

from django.shortcuts import get_object_or_404, render
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import keyboard
from .models import eBooks
engine = pyttsx3.init()
# audio_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'audio'))
@login_required(login_url='login')
def pdf_to_audio(request, id):
    count = Cart.objects.filter(user=request.user.id).count()
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    global stop_flag
    ebook = get_object_or_404(eBooks, book_id=id)
    audio_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'audio'))
    if not ebook.book_pdf:
        return render(request, 'error.html', {'message': 'PDF not found'})
    pdf_reader = PyPDF2.PdfReader(BytesIO(ebook.book_pdf.read()))
    num_pages = len(pdf_reader.pages)
    text = ''
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        engine.save_to_file(text, temp_file.name)
        print(os.path.exists(temp_file.name))
        temp_file.flush()
        os.fsync(temp_file.fileno())
        audio_filename = os.path.basename(temp_file.name)
        temp_file.close()
    with open(temp_file.name, 'rb') as f:
        audio_data = f.read()
    audio_content = ContentFile(audio_data)
    print(len(audio_data))

    ebook.book_audioFile.save(audio_filename, audio_content)
    print('Temp file:', temp_file.name)
    print('Audio file:', audio_filename)
    # Render the template

    # Get the URL of the saved audio file
    audio_file_url = audio_storage.url(ebook.book_audioFile.name)
    engine.stop()
    engine.say(text)
    print(audio_data)
    if stop_flag:
        engine.stop()
        stop_flag = False
    # engine.runAndWait()
    print('audio_file_url:', audio_file_url)
    return render(request, 'pdf_to_audio.html', {'audio_file_url': audio_file_url,'count':count,'w_count':w_count})
import threading
stop_flag = False
def run(request):
    count = Cart.objects.filter(user=request.user.id).count()
    w_count = Whishlist.objects.filter(user=request.user.id).count()
    global stop_flag
    while not stop_flag:
        engine.runAndWait()
    return render(request, 'pdf_to_audio.html',{'count':count,'w_count':w_count})

def stop(request):
    global stop_flag
    stop_flag = True
    engine.setProperty('rate', 0)
    engine.stop()
    # engine.stop()
    return render(request, 'pdf_to_audio.html')
def pause(request):
    engine.pause()

    return redirect('pdf_to_audio')
def resume(request):
    engine.resume()
    return redirect('pdf_to_audio')
# import pyttsx3
# import spacy
# import en_core_web_sm
# # Load the English NLP model from spaCy
# nlp = spacy.load('en_core_web_sm')

# # Initialize the pyttsx3 text-to-speech engine
# engine = pyttsx3.init()

# def pdf_to_audio(request, id):
#     # Load the PDF file from the database
#     ebook = get_object_or_404(eBooks, book_id=id)
#     if not ebook.book_pdf:
#         return render(request, 'error.html', {'message': 'PDF not found'})

#     # Extract the text from the PDF using PyPDF2
#     pdf_reader = PyPDF2.PdfReader(BytesIO(ebook.book_pdf.read()))
#     num_pages = len(pdf_reader.pages)
#     text = ''
#     for page_num in range(num_pages):
#         page = pdf_reader.pages[page_num]
#         text += page.extract_text()

#     # Process the text using spaCy to extract named entities
#     doc = nlp(text)
#     entities = [ent.text for ent in doc.ents]

#     # Convert the entities to speech using pyttsx3
#     engine.setProperty('rate', 150)
#     for entity in entities:
#         engine.say(entity)

#     # Save the audio file to the book_audioFile field on the eBooks model
#     with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
#         engine.save_to_file(text, temp_file.name)
#         temp_file.flush()
#         os.fsync(temp_file.fileno())
#         audio_filename = os.path.basename(temp_file.name)
#     with open(temp_file.name, 'rb') as f:
#         audio_data = f.read()
#     audio_content = ContentFile(audio_data)
#     ebook.book_audioFile.save(audio_filename, audio_content)

#     # Get the URL of the saved audio file
#     audio_file_url = audio_storage.url(ebook.book_audioFile.name)
#     engine.say(text)
#     engine.runAndWait()
#     # Render the template with the audio file URL
#     return render(request, 'pdf_to_audio.html', {'audio_file_url': audio_file_url})

def get(request, id, *args, **kwargs, ):
        place = OrderPlaced.objects.get(id=id)
        date = place.payment.created_at

        orders = OrderPlaced.objects.filter(user_id=request.user.id, payment__created_at=date)
        total = 0
        for o in orders:
            total = total + (o.product.book_price * o.quantity)
        addrs = User.objects.get(id=request.user.id)

        data = {
            "total": total,
            "orders": orders,
            "shipping": addrs,

        }
        pdf = render_to_pdf('report.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # filename = "Report_for_%s.pdf" %(data['id'])
            filename = "Bill.pdf"

            content = "inline; filename= %s" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Page Not Found")








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
        count = Cart.objects.filter(user=request.user).count()
        w_count = Whishlist.objects.filter(user=request.user).count()
        input_text = request.POST.get('input_text', '')
        num_sentences = int(request.POST.get('num_sentences', 5))
        sentences = nltk.sent_tokenize(input_text)
        words = [nltk.word_tokenize(sentence) for sentence in sentences]
        words = [[word for word in sentence if word.isalnum()] for sentence in words]
        summaries = []
        for i in range(len(sentences)):
            score = nltk.sentiment.vader.SentimentIntensityAnalyzer().polarity_scores(sentences[i])['compound']
            print('score',score)
            summaries.append((sentences[i], score))
        summaries = sorted(summaries, key=lambda x: x[1], reverse=True)
        summaries = [summary[0] for summary in summaries[:num_sentences]]
        summary_text = ' '.join(summaries)
        return render(request, self.template_name, {'input_text': input_text, 'summary_text': summary_text, 'num_sentences': num_sentences,'count':count,'w_count':w_count})
# views.py
from django.shortcuts import render
from googletrans import Translator, LANGUAGES


def translation(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')

        # Check if the source and target languages are valid
        if source_language not in LANGUAGES or target_language not in LANGUAGES:
            context = {'error_message': 'Invalid source or target language'}
            return render(request, 'translation.html', context)

        try:
            # Create a Translator object and translate the text to the target language
            translator = Translator()
            translated_text = translator.translate(text, src=source_language, dest=target_language)

            # Render the translated text in the template
            context = {'translated_text': translated_text.text}
            return render(request, 'translation.html', context)
        except Exception as e:
            # Handle any exceptions and display an error message
            context = {'error_message': str(e)}
            return render(request, 'translation.html', context)
    else:
        # Render the initial form with dropdown menus for selecting the source and target languages
        source_language_choices = [(lang_code, lang_name) for lang_code, lang_name in LANGUAGES.items()]
        target_language_choices = [(lang_code, lang_name) for lang_code, lang_name in LANGUAGES.items()]
        context = {'source_language_choices': source_language_choices, 'target_language_choices': target_language_choices}
        return render(request, 'translation.html', context)
