"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path




urlpatterns = [
    path('admin/', admin.site.urls),



    path('', include('myapp.urls')),
    path('', include('news.urls')),
    path('', include('cat.urls')),
    path('', include('subcat.urls')),
    path('', include('contactform.urls')),
    path('', include('trending.urls')),
    path('', include('manager.urls')),
    path('', include('newsletter.urls')),
    path('', include('comments.urls')),
    path('', include('blacklist.urls')),
]