"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from main.views import index, list_internships, add_internship, added_success, \
    register_company, register_successful, apply, application_successful, \
    delete_company, delete_successful, show_internships, update_internship, delete_internship

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('apply/', list_internships),
    path('add/', add_internship),
    path('add/success/', added_success),
    path('register-company/', register_company),
    path('register-company/registration-successful/', register_successful),
    path('apply/form/', apply),
    path('apply/form/application-successful/', application_successful),
    path('delete-company/', delete_company),
    path('delete-company/delete-successful/', delete_successful),
    path('show-internships/', show_internships),
    path('update-internship/', update_internship),
    path('delete-internship/', delete_internship)
]
