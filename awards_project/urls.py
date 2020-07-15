"""awards_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('awards.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/accounts/login/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    #url('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout/", auth_views.LogoutView.as_view()), 
    path(r'^tinymce/', include('tinymce.urls')),
    path(r'^api-token-auth/', obtain_auth_token)
]