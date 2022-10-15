from email.mime import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			messages.warning(request, "you session is allready active")
			return redirect('dashbord')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				messages.warning(request,'You are not authorized to view this page')
				return HttpResponseRedirect('/')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.filter(name = "Secretary")
			return view_func(request, *args, **kwargs)
		
		else:
			messages.warning(request,'You are not authorized to view this page')
			return HttpResponseRedirect('/')
	return wrapper_function