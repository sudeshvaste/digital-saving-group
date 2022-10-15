from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from commitee.decorators import allowed_users
from .forms import EditUserProfileForm, UserRegistrationForm, authorityForm, passwordchangeform
# Create your views here.

@allowed_users(allowed_roles=['Member'])
def user_view(request):
    user = User.objects.all()
    secretary = request.user.groups.filter(name='Secretary')
    president = request.user.groups.filter(name='Precedent')
    accountant = request.user.groups.filter(name='Accountant')
    a = user.filter(is_active=True).count()
    b = user.filter(is_active=False).count()

    fm = UserRegistrationForm()

    context = {
        'form':fm, 'users': user, 'a':a, 'b':b, 'secretary':secretary,
    }

    if request.method == 'POST':
        fm = UserRegistrationForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        if len(password) < 6:
            messages.warning(request, 'Password is too short')
            return HttpResponseRedirect('/user_view')
        if User.objects.filter(username=username).exists():
            messages.warning(request,'User name taken, please use another username')
            return HttpResponseRedirect('/user_view')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already exists, please use another Email id')
            return HttpResponseRedirect('/user_view')

        if fm.is_valid():           
            fm.save()
            messages.success(request,"User created successfully")
            return HttpResponseRedirect('/user_view')
        else:
            messages.success(request,"Details are invalid")
            return HttpResponseRedirect('/user_view')    
    else:
        return render(request, 'commitee/user_view.html', context)
    
@allowed_users(allowed_roles=['Secretary','Member'])
def delete_user(request, id):
    d = User.objects.get(pk=id)     
    if d.last_login is not None:
        d.is_active = False
        messages.warning(request,'User is deactivated because it can not be deleted')
        return HttpResponseRedirect('/user_view')
    else:
        d.delete()
        messages.success(request,'User deleted')
        return HttpResponseRedirect('/user_view')

@allowed_users(allowed_roles=['Secretary','Member'])
def User_profile (request, id):
#    if request.user.is_authenticated:
    user = User.objects.all()
    a = user.filter(is_active=True).count()
    b = user.filter(is_active=False).count()
    pi = User.objects.get(pk=id)
    fm = EditUserProfileForm(instance=pi)
    form = SetPasswordForm(user=pi)
    context = {
        'users': user, 'form':fm, 'form1':form, 'a':a, 'b':b, 
        }
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EditUserProfileForm(request.POST, instance=pi)

        if fm.is_valid():
            fm.save()
            messages.success(request,"Profile Updated")
            fm1 = UserRegistrationForm()
            return HttpResponseRedirect('/user_view') 
    return render(request, 'commitee/profile.html', context)

@allowed_users(allowed_roles=['Member'])
def authority(request):
    fm = authorityForm()
    group = Group.objects.all()
    a = group.count
    context = {
        'form':fm,'a':a, 'users': group
        }
    if request.method == 'POST':
        fm = authorityForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"New Authority created successfully")      
        else:
            messages.success(request,"Authority Allready Exists")
    return render(request, 'commitee/authority.html', context)

@allowed_users(allowed_roles=['Secretary','Member'])
def authoritydelete(request, id):
    if request.method == 'POST':
        d = Group.objects.get(pk=id) 
        d.delete()
        fm = authorityForm()
        messages.success(request,"authority Deleted Successfully")
        return HttpResponseRedirect('/authority')
    
@allowed_users(allowed_roles=['Secretary','Member'])
def editauthority(request, name):
    group = Group.objects.all()
    a = group.count
    pi = Group.objects.get(name=name)
    if request.method == 'POST':
        fm = authorityForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request," Authority Updated")
            return HttpResponseRedirect('/authority/', {'form':fm})
        else:
            fm = authorityForm()
            messages.success(request,"Error")
            return HttpResponseRedirect('/authority/', {'form':fm})
    else:
        fm = authorityForm(instance=pi)
        return render(request, 'commitee/authority.html', {'form':fm,'a':a, 'users': group})