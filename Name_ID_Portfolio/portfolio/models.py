from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    full_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile_image/',null=True,blank=True)
    cv_file = models.FileField(upload_to='cv/',null=True,blank=True)
    def __str__(self):
        return self.full_name


class Skill(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    skill_name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=80)
    def __str__(self):
        return self.skill_name


class Education(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    def __str__(self):
        return self.degree


class Experience(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    description = models.TextField()
    def __str__(self):
        return self.position


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/',null=True,blank=True)
    description = models.TextField()
    github_link = models.URLField(blank=True,null=True)
    live_link = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name