from django.db import models
from django.db.models import DateTimeField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.email

class Enrollment(models.Model):
    FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=12)
    Gender = models.CharField(max_length=25)
    Description = models.TextField()
    DOB = models.CharField(max_length=50)
    SelectMembership=models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Refrence = models.CharField(max_length=55)
    Address = models.CharField(max_length=55)
    PaymentStatus = models.CharField(max_length=55,blank=True,null=True)
    Price = models.IntegerField(max_length=55,blank=True,null=True)
    DueDate = DateTimeField(blank = True,null=True)
    timestamp = DateTimeField(auto_now_add=True, blank= True)
    def __str__(self):
        return self.FullName
class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField(max_length=25)
    def __int__(self):
        return self.id
class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=55)
    phone = models.IntegerField(max_length=55)
    salary = models.CharField(max_length=55)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name