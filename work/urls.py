
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('details/(?P<username>[\w\-]+)', views.Details, basename='details')
router.register('experience/(?P<username>[\w\-]+)', views.Experience, basename='experience')
router.register('skills/(?P<username>[\w\-]+)', views.Skills, basename='skills')
router.register('projects/(?P<username>[\w\-]+)', views.Projects, basename='projects')
router.register('education/(?P<username>[\w\-]+)', views.Education, basename='education')
router.register('personalskills/(?P<username>[\w\-]+)', views.PersonalSkills, basename='personalskills')
router.register('achievements/(?P<username>[\w\-]+)', views.Achievements, basename='achievements')
router.register('languagesknown/(?P<username>[\w\-]+)', views.LanguagesKnown, basename='languagesknown')
router.register('interests/(?P<username>[\w\-]+)', views.Interests, basename='interests')
router.register('cards/(?P<username>[\w\-]+)', views.Cards, basename='cards')

urlpatterns = [
    path('', include(router.urls)),
]
