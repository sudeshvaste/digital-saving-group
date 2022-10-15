from django.apps import AppConfig
from django.urls import path
from . import views
import account

AppConfig = "account"
urlpatterns = [
    path('loan/', views.loan, name='loan'),
    path('approve/<int:id>/<str:Authority>', views.approve, name='approve'),
    path('decline/<int:id>/<str:Authority>', views.decline, name='decline'),
    path('loan_details/<int:id>', views.loan_details, name='loan_details'),
    path('overview/', views.overview, name='overview'),
    path('expenditures/', views.expenditures, name='expenditures'),
    path('delete_exp/<int:id>/', views.delete_exp, name='delete_exp'),
]
