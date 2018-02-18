from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User 


class Devices(models.Model):
	coreid = models.CharField(max_length=24, unique=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class PhoneNumber(models.Model):
	phone_num = models.CharField(max_length=11)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# class Client(User):
# 	phone_num = models.CharField(max_length=11)


# 	class Meta:
# 		proxy = True


