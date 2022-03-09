
from django import forms  
from  doctorApp.models import Doctor,Patient  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  ,UserChangeForm
from django.core.exceptions import ValidationError  

  
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'form-control',}))  
    first_name = forms.CharField(label='First Name', max_length=150,widget=forms.TextInput(attrs={'class':'form-control',}))  
    last_name = forms.CharField(label='Last Name', max_length=150,  widget=forms.TextInput(attrs={'class':'form-control',})) 
    # City= forms.CharField(label='City', max_length=150,  widget=forms.TextInput(attrs={'class':'form-control',})) 
    # address = forms.CharField(label='Address', max_length=550,  widget=forms.Textarea(attrs={'class':'form-control',})) 
    # age= forms.IntegerField(label='Age',  widget=forms.TextInput(attrs={'class':'form-control',})) 
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control',}))  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control',}))  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control',}))  
    class Meta:
        model=User
        
      
        fields = ['first_name', 'last_name','username','email','password1','password2']
   