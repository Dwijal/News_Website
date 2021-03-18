from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
import datetime
import news
from .models import Blacklist
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User , Group, Permission
from manager.models import Manager
import random
import string

def black_list(request):

    ip = Blacklist.objects.all()


    return render(request, 'back/black_list.html',{'ip':ip})


def add_ip(request):

    if request.method == 'POST':
        ip = request.POST.get('ip')
        if ip != '':
            b = Blacklist(ip=ip)
            b.save()


    return redirect('black_list')

def del_ip(request,id):

    b = Blacklist.objects.filter(pk=id)
    b.delete()


    return redirect('black_list')
