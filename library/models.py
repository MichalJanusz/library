from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    pub_date = models.DateField()
    isbn = models.IntegerField(unique=True)
    pages = models.IntegerField()
    cover = models.URLField(blank=True)
    lang = models.CharField(max_length=16)

    def get_absolute_url(self):
        return f'/book/{self.id}'
