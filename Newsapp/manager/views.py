from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
import datetime
import news
from .models import Manager
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User , Group, Permission
from django.contrib.contenttypes.models import  ContentType



def manager_list(request):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    manager = Manager.objects.all().exclude(uname='Admin')

    return render(request, 'back/manager_list.html',{'manager':manager})


def manager_del(request, id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    manager = Manager.objects.get(pk=id)
    b = User.objects.filter(username=manager.uname)
    b.delete()

    manager.delete()



    return redirect('manager_list')




def manager_group(request):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    group = Group.objects.all().exclude(name='masteruser')
    return render(request, 'back/manager_group.html',{'group':group})

def manager_group_add(request):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    if request.method == 'POST':

        gname = request.POST.get('groupname')

        if gname != "":

            if len(Group.objects.filter(name=gname))==0:
                group = Group(name=gname)
                group.save()







    return redirect('manager_group')




def manager_group_del(request, name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    b = Group.objects.filter(name=name)
    b.delete()

    return redirect('manager_group')

def user_group(request,id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    manager = Manager.objects.get(pk=id)
    user = User.objects.get(username=manager.name)
    print(manager.name)
    ugroup = []
    for i in user.groups.all():

        ugroup.append(i.name)
    group = Group.objects.all()

    return render(request, 'back/user_group.html', {'ugroup':ugroup, 'group':group,'id':id })



def add_user_to_groups(request,id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    if request.method ==  'POST':

        ugname = request.POST.get('ugname')

        group = Group.objects.get(name=ugname)
        manager = Manager.objects.get(pk=id)
        user = User.objects.get(username=manager.name)
        user.groups.add(group)


    return redirect('user_group',id)



def del_user_to_groups(request,id,name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})



    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=id)
    user = User.objects.get(username=manager.name)
    user.groups.remove(group)


    return redirect('user_group',id)


def manager_perms(request):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    perms = Permission.objects.all()
    return render(request, 'back/manager_perms.html',{'perms':perms})


def manager_perms_del(request, name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    perms = Permission.objects.filter(name=name)
    perms.delete()

    return redirect('manager_perms')

def manager_perms_add(request):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    if request.method ==  'POST':

        permsname = request.POST.get('permsname')
        codename = request.POST.get('codename')

        if len(Permission.objects.filter(codename=codename)) == 0:
            content_type = ContentType.objects.get(app_label='myapp', model='article')
            Permission.objects.create(codename=codename,name=permsname ,content_type=content_type)
        else:
            error = 'Duplicate Entry Exists'
            return render(request, 'back/error.html', {'error':error})






    return redirect('manager_perms')


def user_perms(request,id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    manager = Manager.objects.get(pk=id)
    user = User.objects.get(username=manager.name)

    permission = Permission.objects.filter(user=user)
    uperms = []
    print(permission)
    for i in permission:

        uperms.append(i.name)

    perms = Permission.objects.all()





    return render(request, 'back/user_perms.html', {'uperms':uperms, 'id':id, 'perms':perms })


def user_perms_del(request,id, name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})


    manager = Manager.objects.get(pk=id)
    user = User.objects.get(username=manager.name)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)


    return redirect('user_perms',id)

def user_perms_add(request,id):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    if request.method == 'POST':
        paname = request.POST.get('pname')

        manager = Manager.objects.get(pk=id)
        user = User.objects.get(username=manager.name)

        permission = Permission.objects.get(name=paname)
        user.user_permissions.add(permission)


    return redirect('user_perms',id)


def groups_perms(request,name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    group = Group.objects.get(name=name)
    perms = group.permissions.all()
    allperms = Permission.objects.all()

    return render(request, 'back/groups_perms.html', {'perms':perms, 'name':name, 'allperms':allperms})


def groups_perms_del(request,gname,name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)

    group.permissions.remove(perm)


    return redirect('groups_perms', name=gname)


def groups_perms_add(request,name):
    # Login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #Login CHeck Ends HERE

    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser' : prem = 1

    if prem ==0 :
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error':error})

    if request.method == 'POST':
        pname = request.POST.get('pname')
        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)

        group.permissions.add(perm)


    return redirect('groups_perms', name=name)

