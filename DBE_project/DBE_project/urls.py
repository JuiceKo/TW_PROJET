"""
URL configuration for DBE_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from chat_app import views


urlpatterns = [
    path('', views.index_view, name='index'),        
    path('chatroom/', views.chatroom_view, name='chatroom'),  
    path('login/', views.login_view, name='login'),    
    path('register/', views.register_view, name='register'),  
    path('creer-groupe/', views.creer_groupe, name='creer_groupe'),
    path('ajouter-ami/', views.ajouter_ami, name='ajouter_ami'),
]

