import json
from django.shortcuts import render
from core.models import Product, ContactUs
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'core/index.html',context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    p_image = product.p_images.all()
    context = {
        'product': product,
        'p_image': p_image,
    }
    return render(request, 'core/product-detail.html',context)

def ajax_contact_form(request):
    full_name = request.GET.get("full_name")
    email = request.GET.get("email")
    phone = request.GET.get("phone")
    message = request.GET.get("message")
    
    from_email = settings.DEFAULT_FROM_EMAIL
    contact, _ = ContactUs.objects.get_or_create(full_name=full_name, email=email, phone=phone, message=message)
    context = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "message": message
    }
    email_template = "emails/contact_email_template.html"
    message = render_to_string(email_template, context)
    subject = "Có khách hàng mới quan tâm dự án của bạn"
    to_email = settings.ADMIN_EMAIL
    mail = EmailMessage(subject, message, from_email, to=[to_email])
    mail.send()
    
    return JsonResponse({
        "success": True,
        "message": " Message sent successfully."
    })