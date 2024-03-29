from django.db import models
from django.contrib.gis.db import models as GeoModels
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    id = models.AutoField(verbose_name='记录编号',primary_key=True)
    userName = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    class Meta:
        db_table = "users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name 
    def __str__(self):
        return self.userName