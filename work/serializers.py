"""
defines serializers for user information models
"""

from rest_framework import serializers
from . import models


class DetailsSerializer(serializers.ModelSerializer):
    """serializes Details model for api"""
    class Meta:
        model = models.Details
        fields = ('id', 'profilePic', 'profilePicPresent', 'profile', 'description', 'city', 'contactNo', 'linkedIn', 'gitHub', 'username')
        

class ExperienceSerializer(serializers.ModelSerializer):
    """serializes Experience model for api"""
    class Meta:
        model = models.Experience
        fields = ('id', 'company', 'profile', 'startdate', 'lastdate', 'city', 'username')


class SkillsSerializer(serializers.ModelSerializer):
    """serializes Skills model for api"""
    class Meta:
        model = models.Skills
        fields = ('id','skill', 'level', 'username')


class ProjectsSerializer(serializers.ModelSerializer):
    """serializes Projects model for api"""
    class Meta:
        model = models.Projects
        fields = ('id','title', 'description', 'username')


class EducationSerializer(serializers.ModelSerializer):
    """serializes Education model for api"""
    class Meta:
        model = models.Education
        fields = ('id','course', 'institution', 'startdate', 'lastdate', 'city', 'username')


class PersonalSkillsSerializer(serializers.ModelSerializer):
    """serializes Personal Skills model for api"""
    class Meta:
        model = models.PersonalSkills
        fields = ('id','skill', 'username')


class AchievementsSerializer(serializers.ModelSerializer):
    """serializes Achievements model for api"""
    class Meta:
        model = models.Achievements
        fields = ('id','description', 'date', 'username')


class LanguagesKnownSerializer(serializers.ModelSerializer):
    """serializes Languages Known model for api"""
    class Meta:
        model = models.LanguagesKnown
        fields = ('id','language', 'readlevel', 'writelevel', 'username')


class InterestsSerializer(serializers.ModelSerializer):
    """serializes Interests model for api"""
    class Meta:
        model = models.Interests
        fields = ('id','interest', 'username')


class CardsSerializer(serializers.ModelSerializer):
    """serializes Cards model for api"""
    class Meta:
        model = models.Cards
        fields = ('id', 'username', 'experience', 'projects', 'education', 'skills', 'personalskills', 'languagesknown', 'interests', 'achievements')