"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#looking in music directory for views.py to import all views from that file 
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
#at the root path run the view called list_albums
    path("", list_albums, name='list_albums')
] 
#review amy's URL committ.  add url's in two places in the From/import and then in the URL patterns
