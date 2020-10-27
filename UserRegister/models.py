from django.db import models
import datetime
# Create your models here.

class UserList(models.Model):
    user_name = models.CharField(max_length=30, blank=False, primary_key=True)
    register_time = models.DateTimeField(default=datetime.datetime.now())
    user_password = models.CharField(max_length=15, blank=False)
    user_email = models.CharField(max_length=60, blank=False)
    valid = models.BooleanField(default=False)
