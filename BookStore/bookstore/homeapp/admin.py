from django.contrib import admin
from .models import Book,Category,SubCategory,Payment, OrderPlaced,eBooks,BookTypes
from django.http import HttpResponse
import csv
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['book_name','book_quantity','book_price','book_category']
    search_fields = ['book_name']
admin.site.register(Book,BookAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name']
admin.site.register(SubCategory)



class eBookAdmin(admin.ModelAdmin):
    list_display=['ebook_name','book_category','img','book_price','book_pdf','book_type']
    search_fields = ['ebook_name']
admin.site.register(eBooks,eBookAdmin)

class BooktypeAdmin(admin.ModelAdmin):
    list_display = ['book_types']
    search_fields = ['book_types']
admin.site.register(BookTypes,BooktypeAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']
admin.site.register(Category,CategoryAdmin)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['subcategory_name']
# admin.site.register(SubCategory)


# admin.site.register(Payment)





class PaymentAdmin(admin.ModelAdmin):
    def username(self, object):
        return object.user.first_name
    list_display=['username','amount','paid']
    search_fields = ['user']

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
admin.site.register(Payment,PaymentAdmin)
# admin.site.register(OrderPlaced)


def export_log(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="order_details.csv"'
    writer = csv.writer(response)
    writer.writerow(['user', 'ordered_date','product'])
    order_details = queryset.values_list('user', 'ordered_date','product')
    for i in order_details:
        writer.writerow(i)
    return response
export_log.short_description = 'Export to csv'


class OrderPlacedAdmin(admin.ModelAdmin):

    def price(self, object):
        return object.payment.amount
    def username(self, object):
        return object.user.first_name
    list_display=('username','ordered_date','product','price','is_ordered')
    actions = [export_log]

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser
    #
    # def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
    #     context.update({
    #         'show_save': False,
    #         'show_save_and_continue': False,
    #         'show_save_and_add_another': False,
    #         'show_delete': False
    #     })
    #     return super().render_change_form(request, context, add, change, form_url, obj)
    # search_fields = ['ordered_date']
admin.site.register(OrderPlaced,OrderPlacedAdmin)
