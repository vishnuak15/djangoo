from django.db import models
from django.contrib.auth.models import User
from members.models import CustomUser
from django.urls import reverse
import io
from django import forms 
import csv




class Entity(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE) 
    entity_name = models.CharField(max_length=264)
    buisness_reg_no = models.IntegerField(unique=True)
    Tax_reg_no = models.IntegerField(unique=True)
    address = models.CharField(max_length = 264)
    reg_date = models.DateField(auto_now_add=True)
    contact_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
            return self.entity_name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})


class UserProfileInfo(models.Model):
    
    REQUIRED_FIELDS = ('CustomUser',)
    
    user = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE,blank=True, null=True)
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE,blank=True, null=True) 
    name = models.CharField(max_length = 264,blank=True, null=True)
    email = models.EmailField(('email address'), unique=True,null=True)
    
    
    def __str__(self):
            return self.name
    
    


class Program(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name ='org' )
    programe_name =  models.CharField(max_length = 264)
    no_of_people = models.PositiveIntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=294)
    description = models.CharField(max_length=294)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.programe_name
    
    def get_absolute_url(self):
        return reverse("program", kwargs={"pk": self.pk})

                        
                
    
