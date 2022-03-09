# Generated by Django 4.0.3 on 2022-03-08 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=40)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('creationDate', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/')),
                ('experience', models.PositiveIntegerField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=40, null=True)),
                ('meetingLink', models.URLField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=40)),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('discription', models.TextField(blank=True, max_length=1000, null=True)),
                ('specialization', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50)),
                ('appointmentTimeChoose', multiselectfield.db.fields.MultiSelectField(choices=[('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'), ('11:00 AM - 12:00 AM', '11:00 AM - 12:00 AM'), ('12:00 AM - 01:00 AM', '12:00 AM - 01:00 AM'), ('01:00 AM - 02:00 AM', '01:00 AM - 02:00 AM')], max_length=79)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(default='none', max_length=500, null=True)),
                ('appointmentTime', models.CharField(max_length=100)),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorApp.doctor')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorApp.patient')),
            ],
        ),
    ]
