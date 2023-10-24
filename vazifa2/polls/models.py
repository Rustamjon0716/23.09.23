from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class AuthorModel(models.Model):
    author_name = models.CharField(max_length=200,default='')
    author_lastname = models.CharField(max_length=200,default='')
    author_birthday = models.DateTimeField(default=datetime.now)
    author_status = models.CharField(max_length=200,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = 'AuthorModel'
    def __str__(self) -> str:
        return self.author_name
    

class BookModel(models.Model):
    book_name = models.CharField(max_length=200,default='')
    book_page = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    description = models.TextField(default='write something!')


    class Meta:
        db_table = 'BookModel'
    def __str__(self) -> str:
        return self.book_name

