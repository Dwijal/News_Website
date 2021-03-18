
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('panel/trending/', views.trending_add, name='trending_add'),
    path('panel/trending/del/<int:id>', views.trending_del, name='trending_del'),
    path('panel/trending/edit/<int:id>', views.trending_edit, name='trending_edit'),
]

