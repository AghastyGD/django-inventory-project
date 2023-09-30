from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Inventory Dashboard'

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)




