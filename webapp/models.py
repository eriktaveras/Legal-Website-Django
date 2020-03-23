from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(default='') 
    img = models.ImageField(upload_to='img')

class Services(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=300)
    content = RichTextField(default=" ")
    img = models.ImageField(upload_to='img')

class CreditRepair(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=300)
    content = RichTextField(default=" ")
    img = models.ImageField(upload_to='img')


class ConsumerLaw(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=300)
    content = RichTextField(default=" ")
    img = models.ImageField(upload_to='img')


def __str__(self):
        return self.title