# from django.contrib.auth.models import User
from statistics import variance
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth import get_user_model
from .logic import varia

from doctorApp.forms import DoctorForm,AppointmentForm
User = get_user_model
# from doctorApp.forms import AppointmentForm
from .models import Doctor,Patient,Appointment
# Create your views here.
def home(request):
    return render(request,'doctorApp/home.html')



appointed=Appointment.objects.values('appointmentTime')
preferred_choice=list(Doctor.objects.filter(id=1).values('appointmentTimeChoose'))
patient=Patient.objects.all()
doctor=Doctor.objects.all()
x=[]
for i in preferred_choice:
        x=i['appointmentTimeChoose']
x=list(x)
y=[]

for j in appointed:
    y.append(''.join(j['appointmentTime']))
y=list(y)
get_from_doctor=[ ]
for i in x:
    if i not in y:
        get_from_doctor.append((str(i),str(i)))




class BookAppointment(CreateView):
    
    form_class=AppointmentForm  
    # model= Appointment 
    # fields=['appointmentDate','doctorId','patientId','patientName']
    # fields='__all__'
    success_url = reverse_lazy('home')
    template_name='doctorApp/book_appointmentC.html'
# --------------------------------------------------------------------------------------------------
    def get_context_data(self, *args,**kwargs):
        context= super().get_context_data(**kwargs)
       
       
        # context['timeslot'] = Doctor.objects.exclude(__in=appointed)
        context['patient'] =patient
        context['doctor'] =doctor
        # context['timeslots'] =timeslots
        context['appointed'] =appointed
        context['x'] =x
        context['y'] =y
        context['xtype'] =type(x)
        context['ytype'] =type(y)
        context['get_from_doctor'] =get_from_doctor
        context['preferred_choice'] =preferred_choice

        # context['timeslot'] = TimeSlot.objects.select_related('appointment')

        # The QuerySet value for an exact lookup must be limited to one result using slicing.

        return context

        # ------------------------------------------------------------------------------------------------
class PatientProfile(CreateView):
   
    # form_class=AppointmentForm  
    model= Patient
    fields='__all__'
    success_url = reverse_lazy('home')
    template_name='doctorApp/patientProfile.html'


class DoctorProfile(CreateView):
   
    # form_class=AppointmentForm  
    model= Doctor 
    # form_class=DoctorForm
    fields='__all__'
    success_url = reverse_lazy('home')
    template_name='doctorApp/doctorProfile.html'

class AllDoctorProfileDisplay(ListView):
    # login_url = 'members/login/'
    # redirect_field_name = 'about'
    model=Doctor
    context_object_name = 'doctor_list'
    template_name = "doctorApp/allDoctorProfileDisplay.html" 
class AllAppointmentDisplay(ListView):
    # login_url = 'members/login/'
    # redirect_field_name = 'about'
    model=Appointment
    context_object_name = 'appointment_list'
    template_name = "doctorApp/allAppointmentDisplay.html" 




# def Appointments(request):
#     if request.method=="POST":
#         patientId=request.POST.get('patientId')
#         doctorId=request.POST.get('doctorId')
#         patientName=request.POST.get('patientName')
#         appointmentDate=request.POST.get('appointmentDate')
#         time=request.POST.get('time')
#         description=request.POST.get('description')
#         print("______________________________________here_______________________________________-")
#         appointed=Appointment.objects.values('time_id')
#         timeslots=TimeSlot.objects.values('id')
#         patient=Patient.objects.all()
#         doctor=Doctor.objects.all()
#         # timeslot = TimeSlot.objects.exclude(id__in=appointed)
#         # context['timeslot'] = TimeSlot.objects.select_related('appointment')

#         # return redirect('index') # redirect calls views.index
#         myuser=Appointment.objects.create_user(patientId,doctorId,patientName,appointmentDate,time,description)
    
#         myuser.save()
#         return render(request,'home.html',{'patient':patient,'doctor':doctor,'timeslot':timeslot})
#     return render(request,'doctorApp/book_appointment.html')