from .models import Appointment,Patient,Doctor 

class Logic():
    preferred_choice=list(Doctor.objects.filter(id=1).values('appointmentTimeChoose'))
    patient=Patient.objects.all()
    doctor=Doctor.objects.all()
    x=[]
    for i in preferred_choice:
            x=i['appointmentTimeChoose']
    x=list(x)
    
    appointed=Appointment.objects.values('appointmentTime')

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


    def get_my_choices(self):
        # you place some logic here
        return self.get_from_doctor
    def get_my_appointed(self):
        # you place some logic here
        return self.y

varia=Logic()
x=varia.get_my_choices()
z=varia.get_my_appointed()