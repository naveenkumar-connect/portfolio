from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
#from django.contrib.auth import get_user_model


class Details(viewsets.ModelViewSet):
    serializer_class = serializers.DetailsSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Details.objects.filter(username = username)


class Experience(viewsets.ModelViewSet):
    serializer_class = serializers.ExperienceSerializer       

    def get_queryset(self):
        username = self.kwargs['username']
        return models.Experience.objects.filter(username = username).order_by('-startdate')


class Skills(viewsets.ModelViewSet):
    serializer_class = serializers.SkillsSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Skills.objects.filter(username = username).order_by('-id')


class Projects(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectsSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Projects.objects.filter(username = username).order_by('-id')


class Education(viewsets.ModelViewSet):
    serializer_class = serializers.EducationSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Education.objects.filter(username = username) .order_by('-startdate')   


class PersonalSkills(viewsets.ModelViewSet):
    serializer_class = serializers.PersonalSkillsSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.PersonalSkills.objects.filter(username = username).order_by('-id')


class Achievements(viewsets.ModelViewSet):
    serializer_class = serializers.AchievementsSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Achievements.objects.filter(username = username).order_by('-date')


class LanguagesKnown(viewsets.ModelViewSet):
    serializer_class = serializers.LanguagesKnownSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.LanguagesKnown.objects.filter(username = username).order_by('-id')


class Interests(viewsets.ModelViewSet):
    serializer_class = serializers.InterestsSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Interests.objects.filter(username = username).order_by('-id')


class Cards(viewsets.ModelViewSet):
    serializer_class = serializers.CardsSerializer        
    
    def get_queryset(self):
        username = self.kwargs['username']
        return models.Cards.objects.filter(username = username) 