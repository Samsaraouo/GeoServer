from django.db import models
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
    
class xiaoban_huzhen(GeoModels.Model):
    geom = GeoModels.GeometryField(null=True,srid=4490)
    dlbm = GeoModels.CharField(max_length=5,null=True,verbose_name="地类编码")
    dlmc = GeoModels.CharField(max_length=60,null=True,verbose_name="地类名称")
    xiao_ban = GeoModels.CharField(max_length=5,null=True,verbose_name="小班代号")
    xbmj = GeoModels.FloatField(null=True,verbose_name="小班面积")
    lin_ban = GeoModels.CharField(max_length=4,null=True,verbose_name="林班")
    lb_name = GeoModels.CharField(max_length=50,null=True,verbose_name="林班名")
    di_ming = GeoModels.CharField(max_length=16,null=True,verbose_name="地名")
    hai_ba = GeoModels.CharField(max_length=4,null=True,verbose_name="海拔")
    cun_name_1 = GeoModels.CharField(max_length=50,null=True,verbose_name="村名")

class yimu(GeoModels.Model):
    geom = GeoModels.PointField(null=True,srid=4490)
    lin_ban = GeoModels.CharField(max_length=4,null=True,verbose_name="林班")
    xiao_ban = GeoModels.CharField(max_length=8,null=True,verbose_name="小班")
    di_lei = GeoModels.CharField(max_length=4,null=True,verbose_name="地类")
    cunname = GeoModels.CharField(max_length=50,null=True,verbose_name="村名")