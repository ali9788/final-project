from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image =  models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=50)
    information = models.CharField(max_length=550)

    def __str__(self):
        return self.name

class Slide(models.Model):
    image =  models.ImageField(upload_to='images')

class Contact(models.Model):
    name = models.CharField('Name',max_length=150, null=True, blank=True)
    email = models.CharField('Email',max_length=150, null=True, blank=True)
    phone = models.CharField('Phone',max_length=150, null=True, blank=True)
    message = models.CharField('Message',max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name}"


