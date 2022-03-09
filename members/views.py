from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm

from doctorApp.forms import DoctorForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy,reverse
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
# from multiuser import settings
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from django.contrib.auth.views import LoginView   
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from doctorApp.models import Doctor,Patient



class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url=reverse_lazy('home') # redirect to home
    # success_message = "You were successfully logged in"

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):   #redirect to home
        return reverse('home')


# class PasswordChangeView(LoginRequiredMixin,PasswordChangeView):
#     form_class=PasswordChangeForm
#     success_message = "User password changed successfully"
#     success_url=reverse_lazy('home')



class PatientRegistrationView(CreateView):
    form_class=CustomUserCreationForm    
    model= Patient
    # fields = '__all__'
    success_url=reverse_lazy('login')
    # success_message = "User registered successfully"
    template_name='registration/patientRegistration.html'

    def get_success_url(self):
        return reverse('home')

class DoctorRegistrationView(CreateView):
    # form_class=CustomUserCreationForm   
    model= Doctor 
    fields = '__all__'
    success_url=reverse_lazy('login')
    # success_message = "User registered successfully"
    template_name='registration/doctorRegistration.html'
    def get_success_url(self):
        return reverse('home')

# class UserRegistrationView(CreateView):
#     form_class=UserCreationForm    
#     success_url=reverse_lazy('login')
#     template_name='registration/registration.html'


class PatientEditView(UpdateView):
    model= Patient 
    fields = '__all__'
    # form_class=CustomUserChangeForm    
    # success_url=reverse_lazy('home')
    template_name='registration/patientEdit.html'
    # success_message = "User edited successfully"

    def get_object(self): #autofill current user data
        return self.request.user
    def get_success_url(self):
        return reverse('home')


class DoctorEditView(UpdateView):
    # model= Doctor 
    # fields = '__all__'
    # form_class=CustomUserChangeForm    
    form_class=DoctorForm
    # success_url=reverse_lazy('home')
    template_name='registration/doctorEdit.html'
    # success_message = "User edited successfully"

    def get_object(self):   #autofill current user data
        return self.request.user
    def get_success_url(self):
        return reverse('home')


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        messages.success(request,'You were successfully logout')
        return render(request, 'registration/logout.html')
        # return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

