"""
defines views for work app
"""

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters


class Details(viewsets.ModelViewSet):
    """ModelViewSet to share user Details model data over API"""
    serializer_class = serializers.DetailsSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Details.objects.filter(username = username)


class Experience(viewsets.ModelViewSet):
    """ModelViewSet to share user Experience model data over API"""
    serializer_class = serializers.ExperienceSerializer       

    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Experience.objects.filter(username = username).order_by('-startdate')


class Skills(viewsets.ModelViewSet):
    """ModelViewSet to share user Skills model data over API"""
    serializer_class = serializers.SkillsSerializer
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Skills.objects.filter(username = username).order_by('-id')


class Projects(viewsets.ModelViewSet):
    """ModelViewSet to share user Projects model data over API"""
    serializer_class = serializers.ProjectsSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Projects.objects.filter(username = username).order_by('-id')


class Education(viewsets.ModelViewSet):
    """ModelViewSet to share user Education model data over API"""
    serializer_class = serializers.EducationSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Education.objects.filter(username = username) .order_by('-startdate')   


class PersonalSkills(viewsets.ModelViewSet):
    """ModelViewSet to share user PersonalSkills model data over API"""
    serializer_class = serializers.PersonalSkillsSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.PersonalSkills.objects.filter(username = username).order_by('-id')


class Achievements(viewsets.ModelViewSet):
    """ModelViewSet to share user Achievements model data over API"""
    serializer_class = serializers.AchievementsSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Achievements.objects.filter(username = username).order_by('-date')


class LanguagesKnown(viewsets.ModelViewSet):
    """ModelViewSet to share user LanguagesKnown model data over API"""
    serializer_class = serializers.LanguagesKnownSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.LanguagesKnown.objects.filter(username = username).order_by('-id')


class Interests(viewsets.ModelViewSet):
    """ModelViewSet to share user Interests model data over API"""
    serializer_class = serializers.InterestsSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Interests.objects.filter(username = username).order_by('-id')


class Cards(viewsets.ModelViewSet):
    """ModelViewSet to share user Cards model data over API"""
    serializer_class = serializers.CardsSerializer        
    
    def get_queryset(self):
        """shares data of a single user over API whose username is received from the GET request"""
        username = self.kwargs['username']
        return models.Cards.objects.filter(username = username) 