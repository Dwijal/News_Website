
from django.urls import path
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap
from myapp.sitemap import MyNewsSiteMaps

from rest_framework import routers

router = routers.DefaultRouter()
router.register('mynews',views.NewsViewSet)


sitemaps = {
    'new': MyNewsSiteMaps(),
}



urlpatterns = [

    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('', views.index, name='home'),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),

    path('about/', views.about, name='about'),
    path('panel/', views.admin_panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('register/', views.myregister, name='myregister'),
    path('logout/', views.mylogout, name='mylogout'),
    path('panel/settings/', views.site_settings, name='site_settings'),
    path('panel/about/settings/', views.about_settings, name='about_settings'),
    path('panel/change/pass/', views.change_pass, name='change_pass'),
    path('contact/', views.contact, name='contact'),
    path('json/data/', views.data_jason, name='data_jason'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
