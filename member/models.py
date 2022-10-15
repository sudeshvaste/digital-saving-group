
from django.db import models
from django.contrib.auth.models import User

from member.email import forgrt_pwd_send_email
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_pwd_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username