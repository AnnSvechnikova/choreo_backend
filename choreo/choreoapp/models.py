from django.db import models
from django.conf import settings
from django.contrib import admin
from django.utils import timezone
# Create your models here.


class Dancer(models.Model):
    dancer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    number = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'books'

    def __str__(self):
        return self.name or ' '
