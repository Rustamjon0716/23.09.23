from django.db import models
from datetime import datetime
# Create your models here.

class task_name(models.Model):
    task_name_text = models.CharField(max_length=200,default='')
    pub_date = models.DateTimeField(default=datetime.now)
    task_name_ptich = models.CharField(max_length=100,default='')
    status = models.BooleanField()

