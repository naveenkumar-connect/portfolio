"""
defines serializers for custom user profile, token and other user details
"""

from rest_framework import serializers
from . import models
from rest_framework.authtoken.models import Token


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes custom user model for api"""

    class Meta:
        model = models.UserProfile

        #field required to be shared over api
        fields = ('username', 'email', 'name', 'password')

        #making password write only over api
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'} 
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user over api"""

        user = models.UserProfile.objects.create_user(
            username = validated_data['username'],
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """function updates new user over api"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)
        

class TokenSerializer(serializers.ModelSerializer):
    """serializes custom user model for api"""

    class Meta:
        model = Token
        fields = ('user_id', 'key', 'created')


class PasswordSerializer(serializers.Serializer):
    """serializes fields for password reset api"""
    username = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class GetTokenSerializer(serializers.Serializer):
    """serializes token to be shared over api"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
        

class UsernameCheckSerializer(serializers.ModelSerializer):
    """serializes username to be shared over api"""
    class Meta:
        model = models.UserProfile
        fields = ('username',)


class EmailCheckSerializer(serializers.ModelSerializer):
    """serializes email to be shared over api"""
    class Meta:
        model = models.UserProfile
        fields = ('email',)