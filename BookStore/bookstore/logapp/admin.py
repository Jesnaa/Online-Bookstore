from django.contrib import admin
from .models import User
import csv
from django.http import HttpResponse
from django.contrib.auth.models import Group
# Register your models here.
# admin.site.register(User)

admin.site.unregister(Group)
def export_log(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_details.csv"'
    writer = csv.writer(response)
    writer.writerow(['Usename', 'Phonenumber','Email'])
    user_details = queryset.values_list('first_name', 'phonenumber','email')
    for i in user_details:
        writer.writerow(i)
    return response
export_log.short_description = 'Export to csv'
class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','email','phonenumber']
    actions = [export_log]
admin.site.register(User, UserAdmin)
