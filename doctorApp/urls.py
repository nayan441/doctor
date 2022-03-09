"""drAppointment URL Configuration

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

from django.urls import path
from doctorApp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('appointmentPage',views.BookAppointment.as_view(),name='appointmentPage'),
    # path('appointment',views.Appointments,name='appointment'),
    path('patientProfile',views.PatientProfile.as_view(),name='patientProfile'),
    path('doctorProfile',views.DoctorProfile.as_view(),name='doctorProfile'),
    path('allDoctorProfileDisplay',views.AllDoctorProfileDisplay.as_view(),name='allDoctorProfileDisplay'),
    path('allAppointmentDisplay',views.AllAppointmentDisplay.as_view(),name='allAppointmentDisplay'),
   
]
