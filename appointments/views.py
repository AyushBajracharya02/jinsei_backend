from django.http import JsonResponse
from my_models.models import Appointment, Doctor, AppUser, Prescription
from django.db.models import OuterRef
from django.http import QueryDict
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


def appointments(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    doctor = Doctor.objects.filter(id=requestData["doctorId"]).first()
    appointments = Appointment.objects.filter(
        doctor=doctor, date=requestData["date"]
    ).order_by("time")
    appointments = [model_to_dict(appointment) for appointment in appointments]
    return JsonResponse({"appointments": appointments})


@csrf_exempt
def bookAppointment(request):
    if request.method == "POST":
        data = request.body.decode("utf-8")
        data = json.loads(data)
        user = False
        if data['isdoctor']:
            user = Doctor.objects.get(id = data["userId"])
        else:
            user = AppUser.objects.get(id = data["userId"])
        doctor = get_object_or_404(Doctor, id=data["doctorId"])
        if not doctor:
            return JsonResponse({"booking": False})
        time_object = datetime.strptime(data["time"], "%I:%M %p").time()
        appointment = Appointment(date=data["date"], time=time_object, doctor=doctor)
        if data['isdoctor']:
            appointment.content_type = ContentType.objects.get_for_model(Doctor)
        else:
            appointment.content_type = ContentType.objects.get_for_model(AppUser)
        appointment.object_id = data["userId"]
        appointment.save()
        return JsonResponse({"booking": True})


def upcomingappointments(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    converted_dict = {}
    for key, value in requestData.items():
        if value.isdigit():
            converted_dict[key] = int(value)
        elif value.lower() == "true":
            converted_dict[key] = True
        elif value.lower() == "false":
            converted_dict[key] = False
        else:
            converted_dict[key] = value
    content_type = ContentType.objects.get_for_model(AppUser)
    if converted_dict["isdoctor"]:
        content_type = ContentType.objects.get_for_model(Doctor)
    appointments = Appointment.objects.filter(
        content_type=content_type, object_id=converted_dict["userId"]
    )
    appointments = appointments.exclude(
        id__in=Prescription.objects.filter(appointment_id=OuterRef("id")).values(
            "appointment_id"
        )
    )
    appointments = [model_to_dict(appointment) for appointment in appointments]
    doctors = []
    for appointment in appointments:
        doctors.append(model_to_dict(Doctor.objects.get(id=appointment["doctor"])))
    appointmentsaspatient = []
    for i in range(len(appointments)):
        appointmentsaspatient.append(
            {
                "appointmentdetails": {
                    "appointment": appointments[i],
                    "doctor": doctors[i],
                }
            }
        )
    if not converted_dict["isdoctor"]:
        return JsonResponse({"appointmentsaspatient": appointmentsaspatient})
    appointments = Appointment.objects.filter(doctor=converted_dict["userId"])
    appointments = appointments.exclude(
        id__in=Prescription.objects.filter(appointment_id=OuterRef("id")).values(
            "appointment_id"
        )
    )
    patients = []
    for appointment in appointments:
        if ContentType.objects.get_for_model(
            appointment.patient
        ) == ContentType.objects.get_for_model(AppUser):
            patients.append(
                model_to_dict(AppUser.objects.get(id=appointment.object_id))
            )
        else:
            patients.append(model_to_dict(Doctor.objects.get(id=appointment.object_id)))
    appointmentsasdoctor = []
    for i in range(len(appointments)):
        appointmentsasdoctor.append(
            {
                "appointmentdetails": {
                    "appointment": model_to_dict(appointments[i]),
                    "patient": patients[i],
                }
            }
        )
    return JsonResponse(
        {
            "appointmentsaspatient": appointmentsaspatient,
            "appointmentsasdoctor": appointmentsasdoctor,
        }
    )


def prescriptionHistory(req):
    requestData = req.GET.urlencode()
    requestData = dict(req.GET)
    content_type = ContentType.objects.get_for_model(AppUser)
    if requestData["isdoctor"][0] == "true":
        content_type = ContentType.objects.get_for_model(Doctor)
    appointmentWithPrescriptions = Appointment.objects.filter(
        content_type=content_type,
        object_id=int(requestData["id"][0]),
        prescription__isnull=False,
    )
    appointmentWithPrescriptionsDict = [model_to_dict(appointment) for appointment in appointmentWithPrescriptions]
    doctors = []
    for appointment in appointmentWithPrescriptionsDict:
        doctors.append(model_to_dict(Doctor.objects.get(id=appointment["doctor"])))
    appointmentdetails = []
    for i in range(len(appointmentWithPrescriptionsDict)):
        appointmentdetails.append(
            {
                "appointmentdetails": {
                    "appointment": appointmentWithPrescriptionsDict[i],
                    "doctor": doctors[i],
                }
            }
        )
    return JsonResponse({"appointments": appointmentdetails})
