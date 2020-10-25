"""
creates models for work app
"""

from datetime import date
from django.db import models


class Details(models.Model):
    """Database model for users details in the system"""
    profilePic = models.ImageField(upload_to='images/', blank=True, null=True)
    profilePicPresent = models.BooleanField(default=False);
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    profile = models.CharField(max_length=50,default="", blank = True)
    description = models.CharField(max_length=50, default="", blank = True)
    city = models.CharField(max_length=20, default="", blank = True)
    contactNo = models.CharField(max_length=15, default="", blank = True)
    linkedIn = models.CharField(max_length = 200, default="", blank = True)
    gitHub = models.CharField(max_length = 200, default="", blank = True)
    


class Experience(models.Model):
    """Database model for users experience in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    company = models.CharField(max_length=30,default="")
    profile = models.CharField(max_length=50,default="")
    startdate = models.DateField(default=date.today)
    lastdate = models.DateField(default=date.today)
    city = models.CharField(max_length=20,default="")
    

class Skills(models.Model):
    """Database model for users skills in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    LEVELS = (
        ('Advanced','Advanced'),
        ('Intermediate','Intermediate'),
        ('Beginner','Beginner'),
    )
    skill = models.CharField(max_length=30, default="")
    level = models.CharField(max_length=12, choices = LEVELS, default='Beginner')


class Projects(models.Model):
    """Database model for users projects in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default="")
    description = models.CharField(max_length=100,default="")


class Education(models.Model):
    """Database model for users education in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    course = models.CharField(max_length=20,default="")
    institution = models.CharField(max_length=50,default="")
    startdate = models.DateField(default=date.today)
    lastdate = models.DateField(default=date.today)
    city = models.CharField(max_length=20,default="")


class PersonalSkills(models.Model):
    """Database model for users personal skills in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    skill = models.CharField(max_length=20,default="")
    

class Achievements(models.Model):
    """Database model for users achievements in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    description = models.CharField(max_length=50,default="")
    date = models.DateField(default=date.today)


class LanguagesKnown(models.Model):
    """Database model for users languages known in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    language = models.CharField(max_length=20,default="")
    LEVELS = (
        ('Advanced','Advanced'),
        ('Intermediate','Intermediate'),
        ('Beginner','Beginner'),
    )
    readlevel = models.CharField(max_length=12, choices = LEVELS, default='Beginner')
    writelevel = models.CharField(max_length=12, choices = LEVELS, default='Beginner')


class Interests(models.Model):
    """Database model for users interests in the system"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    interest = models.CharField(max_length=20,default="")


class Cards(models.Model):
    """Database model to keep a track of users selected cards"""
    username = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
    experience = models.BooleanField(default=False)
    projects = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    skills = models.BooleanField(default=False)
    personalskills = models.BooleanField(default=False)
    languagesknown = models.BooleanField(default=False)
    interests = models.BooleanField(default=False)
    achievements = models.BooleanField(default=False)