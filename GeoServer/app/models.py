from django.db import models
from django.contrib.gis.db import models as GeoModels
# Create your models here.

class Users(models.Model):
    id = models.AutoField('记录编号',primary_key=True)
     