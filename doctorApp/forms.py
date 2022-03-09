
from django import forms
from django.forms import ModelForm

from .models import Appointment,Doctor,Patient


class DateInput(forms.DateInput):
    input_type = 'date'

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

preferred_choice=list(Doctor.objects.filter(id=1).values('appointmentTimeChoose'))
patient=Patient.objects.all()
doctor=Doctor.objects.all()
x=[]
for i in preferred_choice:
        x=i['appointmentTimeChoose']
x=list(x)
def appoint():
    return Appointment.objects.values('appointmentTime')
appointed=appoint()
y=[]
for j in appointed:
    y.append(''.join(j['appointmentTime']))
y=list(y)
get_from_doctor=[ ]
for i in x:
    if i not in y:
        get_from_doctor.append((str(i),str(i)))
if x.sort()==y.sort() :
    get_from_doctor.append((str('no-appointment'),str('no-appointment')))


def get_my_choices():
    # you place some logic here
    return get_from_doctor

class AppointmentForm(ModelForm):
    # appointed=Appointment.objects.values('time_id')
    # timeslot= TimeSlot.objects.exclude(id__in=appointed)
    appointmentTime=forms.ChoiceField(choices=get_my_choices())
    class Meta:
        model = Appointment
        fields = '__all__'
        # exclude=['appointmentTime']
        widgets = {
            'appointmentDate': DateInput(),
            
        }