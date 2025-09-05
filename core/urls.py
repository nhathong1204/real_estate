from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    
    # # Products detail page
    path('product/<pid>/', views.product_detail_view, name='product-detail'),
    path("ajax-contact-form", views.ajax_contact_form, name="ajax-contact-form"),
]
