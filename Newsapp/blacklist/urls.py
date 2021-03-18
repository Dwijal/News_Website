
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('blacklist/', views.black_list, name='black_list'),
    path('blacklist/add_ip', views.add_ip, name='add_ip'),
    path('blacklist/del_ip/<int:id>', views.del_ip, name='del_ip'),

]
