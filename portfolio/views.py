"""
views for interaction between the react template and the django URL scheme
"""

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serves Single Page Application
index = never_cache(TemplateView.as_view(template_name='index.html'))