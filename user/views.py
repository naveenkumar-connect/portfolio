from . import models, serializers
from . import permissions
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.pagination import PageNumberPagination
from work.models import Details, Experience, Skills, Projects, Education, PersonalSkills, Achievements, LanguagesKnown, Interests, Cards


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnProfile,)

    def get_queryset(self):
        username = self.kwargs['username']
        return models.UserProfile.objects.filter(username = username)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            username = serializer.data["username"]

            Details.objects.create(username_id = username)
            Cards.objects.create(username_id = username)

            return Response({
                'status': 'profileCreated',
                "userData": serializer.data
                }, 
                status=status.HTTP_201_CREATED, 
                headers=headers
            )
        else:
            return Response( {
                'status': 'improperUsernameAndEmail',
                'err': serializer.errors
                }, 
                status=status.HTTP_200_OK
            )
        

class PaginationResult(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class SearchProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'name',)
    queryset = models.UserProfile.objects.all()
    pagination_class = PaginationResult

"""
class UserLoginApiView(ObtainAuthToken):
    Handle creating user authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
"""

class UserLogoutViewSet (viewsets.ModelViewSet):
    """Logging out a user by deleting the Auth Token"""

    serializer_class = serializers.TokenSerializer
    queryset = Token.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.DeleteOwnToken,)


class UserLoginApiView (APIView):  

    def post(self, request, pk=None): 
        serializer = serializers.GetTokenSerializer(data=request.data)

        if serializer.is_valid(): 
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None :
                user = models.UserProfile.objects.get(username=username)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'status': 'success',
                    'token': token.key
                    }, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response({
                    'status': 'wrongCreds',
                    'comment': 'username or password is wrong'
                    }, 
                    status=status.HTTP_200_OK
                )
        else :
            return Response( {
                'status': 'improperCreds',
                'err': serializer.errors
                }, 
                status=status.HTTP_200_OK
            )
    

class PasswordReset(APIView):

    def put(self, request, pk=None): 
        """Create a hello message with our name""" 
        serializer = serializers.PasswordSerializer(data=request.data) 
        
        if serializer.is_valid(): 
            username = serializer.data.get('username')
            user = authenticate(username=username, password=serializer.data.get('old_password'))
            if user is not None :
                user = models.UserProfile.objects.get(username=username)
                user.set_password(serializer.data.get('new_password'))
                user.save()
                return Response({'status': 'password set'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'wrong old password'}, status=status.HTTP_400_BAD_REQUEST)
            
            
        else: 
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )