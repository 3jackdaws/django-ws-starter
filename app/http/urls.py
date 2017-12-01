"""ott URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token

from app.http.views import common



urlpatterns = [
    # USER PAGE URLS

    url(r'^$', common.index),
    url(r'^static/(.*)', common.static),



    # USER LOGIN/LOGOUT
    url(r'^api/auth/token', obtain_auth_token),



    # EVERYTHING ELSE TO HOME
    url(r'.*', lambda x: HttpResponseRedirect('/')),
]
