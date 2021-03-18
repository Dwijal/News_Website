
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('comments/add/news/<int:id>', views.add_comments, name='add_comments'),
    path('comments/list/', views.comments_list, name='comments_list'),
    path('comments/del/<int:id>', views.comments_del, name='comments_del'),
    path('comments/confirm/<int:id>', views.comments_confirm, name='comments_confirm'),
]
