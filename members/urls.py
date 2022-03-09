
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('patientRegistration',views.PatientRegistrationView.as_view(),name='patientRegistration'),
    path('doctorRegistration',views.DoctorRegistrationView.as_view(),name='doctorRegistration'),
    path('patientEdit',views.PatientEditView.as_view(),name='patientEdit'),
    path('doctorEdit',views.DoctorEditView.as_view(),name='doctorEdit'),
    path('login/',views.LoginView.as_view(),name='login'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/chanmge-password.html'),name='password_change'),
   
]
