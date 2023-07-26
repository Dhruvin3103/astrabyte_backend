from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=300, default="",null=True,blank=True)
    image = models.ImageField(upload_to="image/portfolio/")
    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    message = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name+' '+self.email

class Images(models.Model):
    image = models.ImageField(upload_to="image/img/")

class Founder(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    bio = models.CharField(max_length=300,default="",null=True,blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="image/slave/",null=True,blank=True)
    insta_id = models.URLField(max_length=300,default="",null=True,blank=True)
    fb_id = models.URLField(max_length=300,default="",null=True,blank=True)
    linkedin_url =models.URLField(max_length=300,default="",null=True,blank=True)
    exp = models.CharField(max_length=300,default="",null=True,blank=True)

    def __str__(self) -> str:
        return self.name+' '+self.email
