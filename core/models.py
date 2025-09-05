from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import strip_tags
from userauths.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    pid = ShortUUIDField(unique=True,length=10,max_length=20,alphabet='abcdefgh12345')
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True,blank=True)
    mini_description = models.TextField(default=None, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = 'Products'
        
    def product_description(self):
        return strip_tags(self.description)
    product_description.short_description = "Description"

    def __str__(self) -> str:
        return self.title
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="p_images")
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product Images'

class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"

    def __str__(self) -> str:
        return self.email