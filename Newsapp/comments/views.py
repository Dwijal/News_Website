from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
import datetime
import news
from .models import Comments
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



def add_comments(request,id):

    if request.method == 'POST':

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if (len(str(day)))==1:
            day = '0' + str(day)
        if (len(str(month)))==1:
            month = '0' + str(month)
        today = str(year)+'-'+str(month)+'-'+str(day)
        time = str(now.hour)+':'+str(now.minute)

        comment = request.POST.get('msg')
        if request.user.is_authenticated :
            manager = Manager.objects.get(uname=request.user)
            b =  Comments(name=manager.name,email=manager.email,comments=comment,news_id=id,date=today,time=time)
            b.save()
        else:
            print('I am visiter')
            name = request.POST.get('name')
            email = request.POST.get('email')
            b =  Comments(name=name,email=email,comments=comment,news_id=id,date=today,time=time)
            b.save()


    print('Add comments is being called ')

    username = News.objects.get(pk=id).name

    return redirect('detail',name=username)


def comments_list(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        a = News.objects.get(pk=id).author
        if str(a) != str(request.user) :
            error = 'Access Denied'
            return render(request, 'back/error.html', {'error':error})



    comments = Comments.objects.all()

    return render(request, 'back/comments_list.html', {'comments':comments})


def comments_del(request, id):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        a = News.objects.get(pk=id).author
        if str(a) != str(request.user) :
            error = 'Access Denied'
            return render(request, 'back/error.html', {'error':error})



    comments = Comments.objects.filter(pk=id)
    comments.delete()

    return redirect('comments_list')



def comments_confirm(request, id):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        a = News.objects.get(pk=id).author
        if str(a) != str(request.user) :
            error = 'Access Denied'
            return render(request, 'back/error.html', {'error':error})



    comments = Comments.objects.get(pk=id)
    comments.status = 1
    comments.save()

    return redirect('comments_list')


















