from logapp.models import User
from django.db import models
from django.utils.text import slugify
from django.urls.base import reverse
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}'.format(self.category_name)
    def get_url(self):
        return reverse('category', args=[self.slug])

# category_status = models.BigIntegerField(default=0)
class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    def __str__(self):
        return self.subcategory_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    book_category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT)
    book_quantity = models.BigIntegerField(default=0)
    book_price = models.BigIntegerField(default=0)
    book_oldprice = models.BigIntegerField(default=0)
    book_author = models.CharField(max_length=50)
    book_year = models.BigIntegerField(default=0)
    book_language = models.CharField(max_length=50)
    book_publisher = models.CharField(max_length=100)
    book_status = models.BooleanField(default=True)
    book_desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics', default=0)

    class Meta:
        ordering = ('book_name',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __str__(self):
        return '{}'.format(self.book_name)

    def get_url(self):
        return reverse('product', args=[self.slug])
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Book,on_delete=models.CASCADE)
    product_qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=20,decimal_places=2,default=0)

    def get_product_price(self):
        price=[self.product.price]
        return sum(price)
class Whishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Book,on_delete=models.CASCADE)
#
# class Order(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
#     payment_mode= models.CharField(max_length=100)
#     payment_id = models.CharField(max_length=100, null=True)
#     order_status=(
#         ('pending','pending'),
#         ('out for shipping','out for shipping'),
#         ('delivered','delivered')
#
#     )
#     status = models.CharField(max_length=100,choices=order_status,default='pending' )
#     tracking_no = models.CharField(max_length=100, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return '{}  {}'.format(self.order_id,self.user)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(blank=True,null=True)
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)
# class Order_item(models.Model):
#     orderitem_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.BigIntegerField(default=1)
#     price = models.DecimalField(max_digits=20, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{}  {}'.format(self.orderitem_id, self.product)
class OrderPlaced(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),

    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    is_ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_cost(self):
        return self.quantity


    def __str__(self):
        return str(self.user)