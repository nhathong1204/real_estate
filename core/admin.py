from django.contrib import admin
from core.models import Product, ProductImages, ContactUs

# Register your models here.
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['pid','title','product_description','status']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "message"]

admin.site.register(Product,ProductAdmin)
admin.site.register(ContactUs,ContactUsAdmin)