from django.db import models
from ckeditor.fields import RichTextField

class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, max_length=500, default="")
    content = RichTextField(blank=True, default="")
    img = models.ImageField(upload_to='img')

    class Meta:
        abstract = True 

    def __str__(self):
        return self.title

class AboutUs(BaseModel):
    class Meta:
        verbose_name_plural = "About Us"

class Services(BaseModel):
    class Meta:
        verbose_name_plural = "Services"

class CreditRepair(BaseModel):
    class Meta:
        verbose_name_plural = "Credit Repairs"

class ConsumerLaw(BaseModel):
    class Meta:
        verbose_name_plural = "Consumer Laws"
