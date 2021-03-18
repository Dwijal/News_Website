
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('panel/categories/list/', views.cat_list, name='cat_list'),
    path('panel/categories/add/', views.cat_add, name='cat_add'),
    path('panel/cat/export/', views.export_cat_csv, name='export_cat_csv'),
    path('panel/cat/import/', views.import_csv, name='import_csv'),
]