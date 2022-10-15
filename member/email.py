from django.core.mail import send_mail
from django.conf import settings

def forgrt_pwd_send_email(email, token):
    subject = 'Your forget Password Link'
    message = f'Hi, click on the link to reset your password http://127.0.0.1:8000/password_set2/{token}/'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list)
    return True

def login_email(email):
    subject = 'Login Attempt'
    message = 'Found Login Attempt Recently, click on the link to check http://127.0.0.1:8000/dashbord/'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list)
    return True