
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('contact/submit/', views.contact_add, name='contact_add'),
    path('contact/', views.contact, name='contact'),
    path('panel/contactform/', views.contact_show, name='contact_show'),
    path('panel/contactform/del/<int:id>', views.contact_del, name='contact_del'),
]


