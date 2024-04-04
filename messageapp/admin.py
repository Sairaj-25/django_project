from django.contrib import admin

# Register your models here.
from messageapp.models import Product

# Register your models here.
# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','unit_quantity','pdetails','is_active']
    list_filter=['cat','is_active']
    ordering = ['id'] 

admin.site.register(Product,ProductAdmin)