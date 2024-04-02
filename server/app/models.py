from django.db import models

# Create your models here.
from django.contrib.gis.db import models as GeoModels
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    #定义用户模型，继承自Auth应用的AbstractUser
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
    def __str__(self):
        return self.username