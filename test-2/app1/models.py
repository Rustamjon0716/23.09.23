from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class SiyosiyNewModel(models.Model):
    new_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.new_text

    class Meta:
        db_table = 'siyosiy yangiliklar'

class IjtimoiyNewModels(models.Model):
    new_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.new_text

    class Meta:
        db_table = 'Ijtimoiy Yangiliklar'