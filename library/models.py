from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models


# Create your models here.

def isbn_validator(value):
    if len(str(value)) not in [10, 13]:
        raise ValidationError(
            _('%(value)s is not a valid ISBN number'),
            params={'value': value},
        )


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    pub_date = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(9999)])
    isbn = models.BigIntegerField(unique=True, verbose_name='ISBN',
                                  validators=[isbn_validator])
    pages = models.IntegerField(verbose_name='Number of pages')
    cover = models.URLField(blank=True, max_length=500, verbose_name='Link to cover')
    lang = models.CharField(max_length=16, verbose_name='Publication language')

    def get_absolute_url(self):
        return f'/book/{self.id}'
