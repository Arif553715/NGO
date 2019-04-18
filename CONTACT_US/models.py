from django.db import models

# Create your models here.



class Artical(models.Model):
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100, default="+880")
    mail=models.CharField(max_length=100)
    posted_on=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.address


class Contact_list(models.Model):
    name=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    message=models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.mail