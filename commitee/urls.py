from django.urls import path
from django.views import View
from . import views
urlpatterns = [
    path('user_view/', views.user_view, name='user_view'),
    path('delete/<int:id>/', views.delete_user, name='deletedata'),
    path('/<int:id>/', views.User_profile, name='userprofile'),
   # path('changepassword/<str:username>/', views.changepassword, name='changepassword'),
    path('authority/', views.authority, name='authority'),
    path('authoritydelete/<int:id>/', views.authoritydelete, name='authoritydelete'),
    path('/<str:name>/', views.editauthority, name='editauthority')
]