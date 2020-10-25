"""
defines url scheme for user app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profile/(?P<username>[\w\-]+)', views.UserProfileViewSet, basename='profile')
router.register('profile', views.UserProfileViewSet, basename='profilecreate')
router.register('searchprofile', views.SearchProfileViewSet, basename='searchprofile')
router.register('logout', views.UserLogoutViewSet)
router.register('usernamecheck/(?P<username>[\w\-]+)', views.UsernameCheckViewSet, basename='usernamecheck')
router.register('emailcheck/(?P<email>[\w.@+-]+)', views.EmailCheckViewSet, basename='emailcheck')

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view() ),
    path('passwordreset/', views.PasswordReset.as_view()),
    path('', include(router.urls) )
]
