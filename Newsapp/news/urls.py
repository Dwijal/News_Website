
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [

    path('news/<str:name>',views.detail, name='detail'),
    path('panel/news/list/',views.news_list, name='news_list'),
    path('panel/news/add/',views.news_add, name='news_add'),
    path('panel/news/del/<int:id>',views.news_delete, name='news_delete'),
    path('panel/news/edit/<int:id>',views.news_edit, name='news_edit'),
    path('panel/news/published/<int:id>',views.news_published, name='news_published'),
    path('urls/<int:pk>',views.detail_shoturl, name='detail_shoturl'),
    path('show/all/news/<str:name>',views.show_all_news, name='show_all_news'),
    path('allnews/allcat/',views.all_news_all_cats, name='all_news_all_cats'),
    path('allnews/allcat/search',views.all_news_all_cat_search, name='all_news_all_cat_search'),


]