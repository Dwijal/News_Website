
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('panel/subcategories/list/', views.subcat_list, name='subcat_list'),
    path('panel/subcategories/add/', views.subcat_add, name='subcat_add'),
]