from django.db import models
from django.utils.text import slugify
from django.urls.base import reverse
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
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
    subcategory_name = models.CharField(max_length=50)
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
