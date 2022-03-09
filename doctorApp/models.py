
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
import datetime
from multiselectfield import MultiSelectField

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
chooseGender=[

('Male','Male'),
('Female','Female'),
('Transgender','Transgender'),
]
timeSlot=[
('10:00 AM - 11:00 AM','10:00 AM - 11:00 AM'),
('11:00 AM - 12:00 AM','11:00 AM - 12:00 AM'),
('12:00 AM - 01:00 AM','12:00 AM - 01:00 AM'),
('01:00 AM - 02:00 AM','01:00 AM - 02:00 AM'),

]

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    experience = models.PositiveIntegerField(blank=True,null=True)
    degree=models.CharField(max_length=40,blank=True,null=True)

    meetingLink=models.URLField(max_length=200,blank=True,null=True)
    gender = models.CharField(max_length=40,choices=chooseGender,default="Male")

    address = models.CharField(max_length=40,null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True)

    discription = models.TextField(max_length=1000,null=True,blank=True)
    specialization= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    
    appointmentTimeChoose=MultiSelectField(choices=timeSlot)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.specialization)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40,null=True,blank=True)
    city = models.CharField(max_length=40,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=40,choices=chooseGender,default="Male")
    mobile = models.CharField(max_length=20,null=True,blank=True)
    creationDate=models.DateField(auto_now=True)
    # symptoms = models.CharField(max_length=100,null=True,blank=True)
    # assignedDoctorId = models.PositiveIntegerField(null=True)
    # admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

# class TimeSlot(models.Model):
#     timeSlot=models.CharField(max_length=50,null=True,blank=True)
#     def __str__(self):
#         return self.timeSlot




class Appointment(models.Model):

    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    patientName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)

    description=models.TextField(max_length=500,null=True,default="none")
    # time=models.OneToOneField(TimeSlot,on_delete=models.DO_NOTHING,default='',null=True,blank=True)
    appointmentTime=models.CharField(max_length=100)

    # status=models.BooleanField(default=False)
 
    def __str__(self):
        # return self.patientId.user.Pat
        return self.patientName
    def get_absolute_url(self):
        return reverse('home')

        
# preferred_choice=[]
# preferred_choice=list(Doctor.objects.filter(id=2).values('appointmentTimeChoose'))
# x=[]
# for i in preferred_choice:
#             x=i['appointmentTimeChoose']
# appointed=Appointment.objects.values('appointmentTime')             
# get_from_doctor=[ ]
# for i in x:
#     if i not in appointed:
#         get_from_doctor.append((i,i))