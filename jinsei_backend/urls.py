"""jinsei_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from login.views import login
from signup.views import signup
from doctors.views import doctors, doctor, doctorTimeScheduleForDay
from appointments.views import appointments, bookAppointment, upcomingappointments
from medicine.views import medicinelist, addPrescription, medication
from dataprovider.views import (
    weight,
    temperature,
    pulserate,
    bloodpressure,
    oxygenlevel,
)
from updateuser.views import updateuser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login),
    path("signup/", signup),
    path("doctors/", doctors),
    path("doctor/", doctor),
    path("doctortimescheduleforday/", doctorTimeScheduleForDay),
    path("appointments/", appointments),
    path("bookappointment/", bookAppointment),
    path("upcomingappointments/", upcomingappointments),
    path("medicinelist/", medicinelist),
    path("addprescription/", addPrescription),
    path("medication/", medication),
    path("weight", weight),
    path("temperature", temperature),
    path("pulse rate", pulserate),
    path("blood pressure", bloodpressure),
    path("oxygen level", oxygenlevel),
    path("updateuser/", updateuser)
]
