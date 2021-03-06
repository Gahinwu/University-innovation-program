"""iot_bag0_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from iot_bag import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('bodybase/', views.bodybase, name='bodybase'),
    path('logout/', views.logout, name='logout'),
    path('MedicalForm/', views.MedicalForm, name='MedicalForm'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('AnotherError/', views.AnotherError, name='AnotherError'),
    path('GFormError/',views.GFormError, name='GFormError'),
    path('PwdError/',views.PwdError, name='PwdError'),
    path('DigestiveSystem/',views.DigestiveSystem, name='DjgestiveSystem'),
    
    
    
    
    
]
