from django.shortcuts import render,get_object_or_404,redirect
from .models import News
from django.core.files.storage import FileSystemStorage
# Create your views here.
import datetime
from subcat.models import SubCat
from cat.models import Cat
from trending.models import Trending
from myapp.models import article
import random
from comments.models import Comments
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from itertools import chain


def detail(request, name):

    article_var =  article.objects.get(pk=6)
    news =  News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews =  News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.get(name=name)

    popularnews =  News.objects.all().order_by('-show')
    popularnews2 =  News.objects.all().order_by('-show')[:3]
    tagsname = News.objects.get(name=name).tags
    tags = tagsname.split(',')
    trending = Trending.objects.all().order_by('-pk')[:5]

    try:
        mynews = News.objects.get(name=name)
        mynews.show = mynews.show + 1
        mynews.save()
    except:
        print('Cant Add Show')

    code = News.objects.get(name=name).pk
    comments = Comments.objects.filter(news_id=code, status=1).order_by('-pk')
    comment_count = len(comments)

    link = 'urls'+str(News.objects.get(name=name).rand)
    return render(request, 'front/detail.html',{'shownews':shownews,'name':article_var, 'News':news, 'cat': cat,'subcat':subcat, 'lastnews':lastnews,'popularnews':popularnews,'popularnews2':popularnews2,"tags":tags,'trending':trending,'code':code,'comments':comments, 'comment_count':comment_count,'link':link,'tagsname':tagsname})



def detail_shoturl(request, pk):

    article_var =  article.objects.get(pk=6)
    news =  News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews =  News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.get(rand=pk)

    popularnews =  News.objects.all().order_by('-show')
    popularnews2 =  News.objects.all().order_by('-show')[:3]
    tagsname = News.objects.get(rand=pk).tags
    tags = tagsname.split(',')
    trending = Trending.objects.all().order_by('-pk')[:5]

    try:
        mynews = News.objects.get(rand=pk)
        mynews.show = mynews.show + 1
        mynews.save()
    except:
        print('Cant Add Show')


    return render(request, 'front/detail.html',{'shownews':shownews,'name':article_var, 'News':news, 'cat': cat,'subcat':subcat, 'lastnews':lastnews,'popularnews':popularnews,'popularnews2':popularnews2,"tags":tags,'trending':trending})













def news_list(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        news = News.objects.filter(author=request.user)
    elif perm == 1 :

        newss = News.objects.all()
        paginator = Paginator(newss,1)
        page = request.GET.get('page')
        try:
            news = paginator.page(page)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            news = paginator.page(1)




    return render(request, 'back/news_list.html', {'News':news})

def news_add(request):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if (len(str(day)))==1:
         day = '0' + str(day)
    if (len(str(month)))==1:
         month = '0' + str(month)
    print(str(year)+'-'+str(month)+'-'+str(day))
    date = str(year)+'-'+str(month)+'-'+str(day)
    randdate = str(year)+str(month)+str(day)
    rand = str(random.randint(1000,9999))
    rand = int(randdate+rand)

    while len(News.objects.filter(rand=rand)) != 0:
        rand = str(random.randint(1000,9999))
        rand = int(randdate+rand)




    cat  = SubCat.objects.all()

    # now = datetime.datetime.now()+datetime.timedelta(days=10)
    # year = now.year
    # month = now.month
    # day = now.day
    # if (len(str(day)))==1:
    #     day = '0' + str(day)
    # if (len(str(month)))==1:
    #     month = '0' + str(month)
    # print(str(year)+'/'+str(month)+'/'+str(day))
    # print('XXXXXXXXXXXXXXXXXXX')

    if request.method == "POST":
        news_title = request.POST.get("newstitle")
        cat = request.POST.get("newscat")
        Summary = request.POST.get("newssum")
        body = request.POST.get("newsbody")
        newsid = request.POST.get("newscat")
        tags = request.POST.get("tags")

        if news_title == "" or Summary == "" or body == "":
            error = "All Fields are required"
            return render(request, 'back/error.html', {'error':error})

        try:

            image = request.FILES['myfiles']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)


            if str(image.content_type).startswith('image'):

                if image.size < 5000000:
                    newsname = SubCat.objects.get(pk=newsid).name
                    ocatid = SubCat.objects.get(pk=newsid).catid


                    data = News(name=news_title, summary=Summary, body=body, date=date, picname=filename, picurl=url, author=request.user, catname=newsname, catid=newsid, ocatid=ocatid, show='0',tags=tags,rand=rand)
                    data.save()

                    count = len(News.objects.filter(ocatid=ocatid))

                    data = Cat.objects.get(pk=ocatid)
                    data.count = count
                    data.save()


                    return redirect('news_list')
                else:
                    error = "Please, Your File Size is bigger than 5 MB"
                    return render(request, 'back/error.html', {'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(str(filename))
                error = "Please Upload Valid Image Format"
                return render(request, 'back/error.html', {'error':error})

        except:

            error = "Please Upload Image"
            return render(request, 'back/error.html', {'error':error})

    return render(request, 'back/news_add.html', {'cat':cat})



def news_delete(request, id):

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


    try:
        b = News.objects.get(pk=id)
        fs = FileSystemStorage()
        fs.delete(str(b.picname))

        ocatid = News.objects.get(pk=id).ocatid

        b.delete()

        count = len(News.objects.filter(ocatid=ocatid))
        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()



    except:
        error = "Something Went Wrong"
        return render(request, 'back/error.html', {'error':error})

    return redirect('news_list')


def news_edit(request,id):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    if len(News.objects.filter(pk=id)) == 0:

        error = "This News Does not Exist"
        return render(request, 'back/error.html', {'error':error})


    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : perm = 1

    if perm == 0:
        a = News.objects.get(pk=id).author
        if str(a) != str(request.user) :
            error = 'Access Denied'
            return render(request, 'back/error.html', {'error':error})








    news = News.objects.get(pk=id)
    cat  = SubCat.objects.all()

    if request.method == "POST":
        news_title = request.POST.get("newstitle")
        Cat = request.POST.get("newscat")
        Summary = request.POST.get("newssum")
        body = request.POST.get("newsbody")
        newsid = request.POST.get("newscat")
        tags = request.POST.get("tags")

        if news_title == "" or Summary == "" or body == "":
            error = "All Fields are required"
            return render(request, 'back/error.html', {'error':error})

        try:

            image = request.FILES['myfiles']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)


            if str(image.content_type).startswith('image'):

                if image.size < 5000000:
                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News.objects.get(pk=id)

                    fss = FileSystemStorage()
                    fss.delete(str(b.picname))

                    b.name = news_title
                    b.summary=Summary
                    b.body=body
                    b.picname=filename
                    b.picurl=url
                    b.catname=newsname
                    b.catid=newsid
                    b.tags = tags
                    b.act = 0
                    b.save()

                    return redirect('news_list')
                else:
                    error = "Please, Your File Size is bigger than 5 MB"
                    return render(request, 'back/error.html', {'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(str(filename))
                error = "Please Upload Valid Image Format"
                return render(request, 'back/error.html', {'error':error})

        except:

            newsname = SubCat.objects.get(pk=newsid).name
            b = News.objects.get(pk=id)

            b.name = news_title
            b.summary=Summary
            b.body=body
            b.catname=newsname
            b.catid=newsid
            b.tags = tags
            b.save()








    return render(request,'back/news_edit.html',{'id':id, 'news':news, 'cat':cat})


def news_published(request, id):

    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    news = News.objects.get(pk=id)
    news.act = 1
    news.save()



    return redirect('news_list')


def show_all_news(request, name):

    catid =  Cat.objects.get(name=name).pk
    allnews = News.objects.filter(ocatid=catid)



    article_var =  article.objects.get(pk=6)

    news =  News.objects.filter(act=1).order_by('-pk')

    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews =  News.objects.filter(act=1).order_by('-pk')[:3]

    popularnews =  News.objects.filter(act=1).order_by('-show')
    popularnews2 =  News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')

    lastnews2 =  News.objects.filter(act=1).order_by('-pk')[:4]




    return render(request, 'front/all_news.html',{'name':article_var, 'News':news, 'cat': cat,'subcat':subcat, 'lastnews':lastnews, 'popularnews2':popularnews2, 'trending':trending,'lastnews2':lastnews2,'allnews':allnews})



def all_news_all_cats(request):

    if request.method == 'POST':
        search = request.POST.get('search')
        catid = request.POST.get('cat')
        f_rom = request.POST.get('from')
        t_o = request.POST.get('to')

        print(f_rom,t_o)







        if catid == '0':
            a = News.objects.filter(name__contains=search)
            b = News.objects.filter(summary__contains=search)
            c = News.objects.filter(body__contains=search)
        else:
            a = News.objects.filter(name__contains=search, ocatid=catid)
            b = News.objects.filter(summary__contains=search,ocatid=catid)
            c = News.objects.filter(body__contains=search,ocatid=catid)

        allnews = list(chain(a,b,c))
        allnews = list(dict.fromkeys(allnews))





    allnews = News.objects.all()
    article_var =  article.objects.get(pk=6)
    news =  News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews =  News.objects.filter(act=1).order_by('-pk')[:3]
    popularnews =  News.objects.filter(act=1).order_by('-show')
    popularnews2 =  News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')
    lastnews2 =  News.objects.filter(act=1).order_by('-pk')[:4]

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if (len(str(day)))==1:
        day = '0' + str(day)
    if (len(str(month)))==1:
        month = '0' + str(month)
    print(str(year)+'-'+str(month)+'-'+str(day))
    date = str(year)+'-'+str(month)+'-'+str(day)
    f_rom= []
    t_o = []

    for i in range(30):
        b = datetime.datetime.now() + datetime.timedelta(days=i)
        year = b.year
        month = b.month
        day = b.day
        if (len(str(day)))==1:
            day = '0' + str(day)
        if (len(str(month)))==1:
            month = '0' + str(month)
        print(str(year)+'-'+str(month)+'-'+str(day))
        b = str(year)+'-'+str(month)+'-'+str(day)
        f_rom.append(b)

        c = datetime.datetime.now() - datetime.timedelta(days=i)
        year = c.year
        month = c.month
        day = c.day
        if (len(str(day)))==1:
            day = '0' + str(day)
        if (len(str(month)))==1:
            month = '0' + str(month)
        print(str(year)+'-'+str(month)+'-'+str(day))
        c = str(year)+'-'+str(month)+'-'+str(day)
        t_o.append(c)






    return render(request, 'front/all_news_all_cat.html',{'name':article_var, 'News':news, 'cat': cat,'subcat':subcat, 'lastnews':lastnews, 'popularnews2':popularnews2, 'trending':trending,'lastnews2':lastnews2,'allnews':allnews,'f_rom':f_rom,'t_o':t_o})



def all_news_all_cat_search(request):

    if request.method == 'POST':
        search = request.POST.get('search')
        catid = request.POST.get('cat')
        f_rom = request.POST.get('from')
        t_o = request.POST.get('to')

        print(f_rom,t_o)
        if f_rom != '0' and t_o != '0' :

            if t_o < f_rom :
                error = "Your Dates are not compatible"
                return render(request, 'front/message.html', {'msg':error})

        if catid == '0':
            if f_rom != '0' and t_o != '0':
                a = News.objects.filter(name__contains=search,date__gte=f_rom,date__lte=t_o)
                b = News.objects.filter(summary__contains=search,date__gte=f_rom,date__lte=t_o)
                c = News.objects.filter(body__contains=search,date__gte=f_rom,date__lte=t_o)
            elif f_rom != '0':
                a = News.objects.filter(name__contains=search,date__gte=f_rom)
                b = News.objects.filter(summary__contains=search,date__gte=f_rom)
                c = News.objects.filter(body__contains=search,date__gte=f_rom)
            elif t_o != '0':
                a = News.objects.filter(name__contains=search,date__lte=t_o)
                b = News.objects.filter(summary__contains=search,date__lte=t_o)
                c = News.objects.filter(body__contains=search,date__lte=t_o)

            else:
                a = News.objects.filter(name__contains=search)
                b = News.objects.filter(summary__contains=search)
                c = News.objects.filter(body__contains=search)
        else:
            if f_rom != '0' and t_o != '0':
                a = News.objects.filter(name__contains=search,date__gte=f_rom,date__lte=t_o)
                b = News.objects.filter(summary__contains=search,date__gte=f_rom,date__lte=t_o)
                c = News.objects.filter(body__contains=search,date__gte=f_rom,date__lte=t_o)
            elif f_rom != '0':
                a = News.objects.filter(name__contains=search,date__gte=f_rom)
                b = News.objects.filter(summary__contains=search,date__gte=f_rom)
                c = News.objects.filter(body__contains=search,date__gte=f_rom)
            elif t_o != '0':
                a = News.objects.filter(name__contains=search,date__lte=t_o)
                b = News.objects.filter(summary__contains=search,date__lte=t_o)
                c = News.objects.filter(body__contains=search,date__lte=t_o)
            else:
                a = News.objects.filter(name__contains=search)
                b = News.objects.filter(summary__contains=search)
                c = News.objects.filter(body__contains=search)

            a = News.objects.filter(name__contains=search, ocatid=catid,date__gte=f_rom,date__lte=t_o)
            b = News.objects.filter(summary__contains=search,ocatid=catid,date__gte=f_rom,date__lte=t_o)
            c = News.objects.filter(body__contains=search,ocatid=catid,date__gte=f_rom,date__lte=t_o)

        allnews = list(chain(a,b,c))
        allnews = list(dict.fromkeys(allnews))

    article_var =  article.objects.get(pk=6)
    news =  News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews =  News.objects.filter(act=1).order_by('-pk')[:3]
    popularnews =  News.objects.filter(act=1).order_by('-show')
    popularnews2 =  News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')
    lastnews2 =  News.objects.filter(act=1).order_by('-pk')[:4]




    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if (len(str(day)))==1:
        day = '0' + str(day)
    if (len(str(month)))==1:
        month = '0' + str(month)
    print(str(year)+'-'+str(month)+'-'+str(day))
    date = str(year)+'-'+str(month)+'-'+str(day)
    f_rom= []
    t_o = []

    for i in range(30):
        b = datetime.datetime.now() + datetime.timedelta(days=i)
        year = b.year
        month = b.month
        day = b.day
        if (len(str(day)))==1:
            day = '0' + str(day)
        if (len(str(month)))==1:
            month = '0' + str(month)
        print(str(year)+'-'+str(month)+'-'+str(day))
        b = str(year)+'-'+str(month)+'-'+str(day)
        f_rom.append(b)

        c = datetime.datetime.now() - datetime.timedelta(days=i)
        year = c.year
        month = c.month
        day = c.day
        if (len(str(day)))==1:
            day = '0' + str(day)
        if (len(str(month)))==1:
            month = '0' + str(month)
        print(str(year)+'-'+str(month)+'-'+str(day))
        c = str(year)+'-'+str(month)+'-'+str(day)
        t_o.append(c)



    return render(request, 'front/all_news_all_cat.html',{'name':article_var, 'News':news, 'cat': cat,'subcat':subcat, 'lastnews':lastnews, 'popularnews2':popularnews2, 'trending':trending,'lastnews2':lastnews2,'allnews':allnews,'f_rom':f_rom,'t_o':t_o})





















