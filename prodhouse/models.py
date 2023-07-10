from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Portfolio(models.Model):
    CHOICES = (
        ('VFX', 'VFX'),
        ('Digital Art', 'Digital Art'),
        ('Games', 'Games'),
    )
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=300, default="")
    image = models.ImageField(upload_to="image/portfolio/")
    project_type = models.CharField(max_length=300,choices=CHOICES,default='past')
    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    message = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name+' '+self.email


class Slave(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    bio = models.CharField(max_length=300,default="")
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="image/slave/")
    insta_id = models.URLField(max_length=300,default="")
    fb_id = models.URLField(max_length=300,default="")
    linkedin_url =models.URLField(max_length=300,default="")
    exp = models.CharField(max_length=300,default="")

    def __str__(self) -> str:
        return self.name+' '+self.email
