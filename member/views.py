
import uuid
from account.models import Loan, Loan_installment, Bachat
from account.form import Aut_Loan_installments, Loan_Application, Loan_installments, BachatForm
from commitee.decorators import admin_only, allowed_users, unauthenticated_user
from .email import forgrt_pwd_send_email, login_email
import random
from django.contrib.auth.models import User
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
# Create your views here.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
b = random.choice(a)
c = random.choice(a)
d = b + c


@unauthenticated_user
def register(request):
    fm = AuthenticationForm()
    context = {
        'form': fm, 'b': b, 'c': c,
    }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']

        if password != password1:
            messages.warning(request, 'password Not Matching')
            return HttpResponseRedirect('/')

        if len(password) < 6:
            messages.warning(request, 'Password is too short')
            return HttpResponseRedirect('/')

        if len(username) < 6:
            messages.warning(request, 'Username is too short')
            return HttpResponseRedirect('/')

        if User.objects.filter(username=username).exists():
            messages.warning(
                request, 'User name taken, please use another username')
            return HttpResponseRedirect('/')

        if User.objects.filter(email=email).exists():
            messages.warning(
                request, 'Email already exists, please use another Email id')
            return HttpResponseRedirect('/')

        else:
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='Member')
            user.groups.add(group)
            messages.success(request, 'User created successfully')
            return HttpResponseRedirect('/')

    return render(request, 'basic/home.html', context)


@unauthenticated_user
def User_login(request):
    if not request.user.is_authenticated:
        fm = AuthenticationForm()
        context = {'b': b, 'c': c, }

        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            e = int(request.POST['answer'])

            if e != d:
                messages.warning(request, 'Capture not Matching')
                return HttpResponseRedirect('/')

            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)

                if user is None:
                    messages.warning(request, "Fill the username and password")
                    return HttpResponseRedirect('/')

                login(request, user)
                messages.success(request, "Logged in sucessfully")

               # login_email(user.email)
                return HttpResponseRedirect('/dashbord/', {'name': request.user})

            else:
                messages.warning(
                    request, "Fill the accurate username and password or User is not Activated")
                return HttpResponseRedirect('/')

        else:
            return render(request, 'basic/home.html', {'form': fm}, context)
    else:
        return HttpResponseRedirect('dashbord/')


@allowed_users(allowed_roles=['Member'])
def User_dashbord(request):
    loan = Loan.objects.filter(member=request.user).order_by("-id")
    bachat = Bachat.objects.filter(member=request.user).order_by("-id")
    fm = Loan_Application()
    fm1 = BachatForm()

    context = {
        'name': request.user, 'loans': loan, 'bachat': bachat, 'form': fm, 'form1': fm1
    }

    if request.method == 'POST':
        fm = Loan_Application(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Request Send Successfully')

    return render(request, 'member/dash1.html', context)


@allowed_users(allowed_roles=['Member'])
def User_logout(request):
    logout(request)
    messages.success(request, "Logged out sucessfully")
    return HttpResponseRedirect('/')


@admin_only
def password_set1(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not User.objects.filter(email=email).exists():
            messages.warning(request, 'Email id not found')
            return HttpResponseRedirect('/password_set1')

        user_obj = User.objects.get(email=email)
#        print(user_obj)
        token = str(uuid.uuid4())
        if Profile.objects.filter(user=user_obj).exists():
            profile_obj = Profile.objects.get(user=user_obj)
        else:
            profile_obj = Profile.objects.create(user=user_obj)

        profile_obj.forget_pwd_token = token
        profile_obj.save()
        forgrt_pwd_send_email(user_obj.email, token)
        messages.success(
            request, 'Password reset link sent to your email successfully')
        return HttpResponseRedirect('/')
    return render(request, 'basic/password_set1.html',)


@allowed_users(allowed_roles=['Member'])
def bachat_appl(request):
    if request.method == 'POST':
        fm1 = BachatForm(request.POST)
        if fm1.is_valid():
            fm1.save()
            messages.success(request, 'Request Send Successfully')
    return HttpResponseRedirect('/dashbord')


@unauthenticated_user
def password_set2(request, token):
    profile_obj = Profile.objects.filter(forget_pwd_token=token).first()
    context = {'user_id': profile_obj.user.id}
    if request.method == 'POST':
        new_password = request.POST['password1']
        confirm_password = request.POST['password2']
        user_id = request.POST.get('user_id')

        if user_id is None:
            messages.warning(request, 'no user id found')
            return HttpResponseRedirect(f'/password_set1')

        if new_password != confirm_password:
            messages.success(request, 'password mismatch')
            return HttpResponseRedirect(f'/password_set1')

        user_obj = User.objects.get(id=user_id)
        user_obj.set_password(new_password)
        user_obj.save()
        token = str(uuid.uuid4())
        profile_obj.forget_pwd_token = token
        profile_obj.save()
        messages.success(request, 'password Reset Successfully')
        return HttpResponseRedirect('/')

    return render(request, 'basic/password_set2.html', context)
