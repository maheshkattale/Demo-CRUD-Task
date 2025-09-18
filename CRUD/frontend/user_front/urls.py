from django.urls import path
from . import views

urlpatterns = [
    # Template rendering URLs
    path('', views.landing_page, name='landing_page'),
]