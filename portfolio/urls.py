"""
portfolio URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/info/', include('work.urls')),
    path('<path:path>/', views.index, name='index'),
    path('', views.index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
