"""
URL configuration for backendproject project.

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
from django.urls import path, include
from backendapp.views import register_staff
from backendapp.views import register_patient
from backendapp.views import get_medecins
from backendapp.views import login_staff
from backendapp.views import login_patient
from backendapp.views import rechercher_patient_par_NSS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register_staff/', register_staff, name='register_staff'),  
    path('api/register_patient/', register_patient, name='register_staff'),  
    path('api/get_medecins/', get_medecins, name='get_medecins'),
    path('api/login_staff/', login_staff, name='login_staff'),
    path('api/login_patient/', login_patient, name='login_patient'),
    path('api/rechercher_nss/', rechercher_patient_par_NSS, name='recherche_nss'),
]
