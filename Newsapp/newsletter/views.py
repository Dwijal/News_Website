from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
import datetime
import news
from .models import Newsletter
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User , Group, Permission
from django.contrib.contenttypes.models import  ContentType


def news_letter(request):

    if request.method == 'POST':
        txt = request.POST.get('txt')
        result = txt.find('@')
        if int(result) != -1:
            b =  Newsletter(txt=txt, status=1)
            b.save()
        else:
            try:
                int(txt)
                b = Newsletter(txt=txt, status=2)
                b.save()
            except:
                return redirect('home')



    return redirect('home')

def news_emails(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    emails = Newsletter.objects.filter(status=1)


    return render(request,'back/emails.html',{'emails':emails})


def news_phones(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    phones = Newsletter.objects.filter(status=2)


    return render(request,'back/phones.html',{'phones':phones})


def news_txt_del(request,id, name):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    b = Newsletter.objects.get(pk=id)
    b.delete()
    if int(name) == 2:
        return redirect('news_phones')

    return redirect('news_emails')


def checkboxlist(request):

    if request.method =='POST':



        # for i in Newsletter.objects.filter(status=1):
        #     # print(i.pk)
        #     x = request.POST.get(str(i.pk))
        #     if str(x) == 'on':
        #         b = Newsletter.objects.get(pk=i.pk)
        #         b.delete()

        #     Second delete Method
        check = request.POST.getlist('check[]')

        for i in check:
            # b = Newsletter.objects.get(pk=i).txt
            b = Newsletter.objects.get(pk=i)
            b.delete()


    # print('Oh, You just submitted the check box querry')

    return redirect('news_emails')
