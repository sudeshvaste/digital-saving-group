from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.User_dashbord, name='dashbord'),
    path('logout/', views.User_logout, name='logout'),
    path('', views.register, name='register'),
    path('login', views.User_login, name='login'),
    path('password_set1/', views.password_set1, name='password_set1'),
    path('password_set2/<token>/', views.password_set2, name='password_set2'),
#    path('password_set/<int:user_id>', views.password_set, name='password_set'),
#    path('password_change/', views.password_change, name='password_change'),
    
    path('bachat_appl/', views.bachat_appl, name='bachat_appl')
]
