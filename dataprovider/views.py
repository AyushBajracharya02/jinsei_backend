from django.http import JsonResponse
from my_models.models import Appointment, Prescription, AppUser, Doctor
from django.forms.models import model_to_dict
from django.http import QueryDict
import json
from django.contrib.contenttypes.models import ContentType


def weight(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    content_type = ContentType.objects.get_for_model(AppUser)
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
    if converted_dict["isdoctor"]:
        content_type = ContentType.objects.get_for_model(Doctor)
    appointments = Appointment.objects.filter(
        content_type=content_type,
        object_id=requestData["id"],
        prescription__isnull=False,
    )
    weightlist = []
    for appointment in appointments:
        prescription = model_to_dict(appointment.prescription_set.first())
        weightlist.append(
            {"date": prescription["createddate"], "weight": prescription["weight"]}
        )
    return JsonResponse({"weightlist": weightlist})


def temperature(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    content_type = ContentType.objects.get_for_model(AppUser)
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
    if converted_dict["isdoctor"]:
        content_type = ContentType.objects.get_for_model(Doctor)
    appointments = Appointment.objects.filter(
        content_type=content_type,
        object_id=requestData["id"],
        prescription__isnull=False,
    )
    temperaturelist = []
    for appointment in appointments:
        prescription = model_to_dict(appointment.prescription_set.first())
        temperaturelist.append(
            {
                "date": prescription["createddate"],
                "temperature": prescription["temperature"],
            }
        )
    return JsonResponse({"temperaturelist": temperaturelist})


def pulserate(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    content_type = ContentType.objects.get_for_model(AppUser)
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
    if converted_dict["isdoctor"]:
        content_type = ContentType.objects.get_for_model(Doctor)
    appointments = Appointment.objects.filter(
        content_type=content_type,
        object_id=requestData["id"],
        prescription__isnull=False,
    )
    pulseratelist = []
    for appointment in appointments:
        prescription = model_to_dict(appointment.prescription_set.first())
        pulseratelist.append(
            {
                "date": prescription["createddate"],
                "pulse rate": prescription["pulse_rate"],
            }
        )
    return JsonResponse({"pulse ratelist": pulseratelist})


def bloodpressure(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    content_type = ContentType.objects.get_for_model(AppUser)
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
    if converted_dict["isdoctor"]:
        content_type = ContentType.objects.get_for_model(Doctor)
    appointments = Appointment.objects.filter(
        content_type=content_type,
        object_id=requestData["id"],
        prescription__isnull=False,
    )
    bloodpressurelist = []
    for appointment in appointments:
        prescription = model_to_dict(appointment.prescription_set.first())
        bloodpressurelist.append(
            {
                "date": prescription["createddate"],
                "blood pressure": prescription["blood_pressure"],
            }
        )
    return JsonResponse({"blood pressurelist": bloodpressurelist})


def oxygenlevel(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    content_type = ContentType.objects.get_for_model(AppUser)
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
    if converted_dict["isdoctor"]:
        content_type = ContentType.objects.get_for_model(Doctor)
    appointments = Appointment.objects.filter(
        content_type=content_type,
        object_id=requestData["id"],
        prescription__isnull=False,
    )
    oxygenlevellist = []
    for appointment in appointments:
        prescription = model_to_dict(appointment.prescription_set.first())
        oxygenlevellist.append(
            {
                "date": prescription["createddate"],
                "oxygen level": prescription["oxygen_level"],
            }
        )
    return JsonResponse({"oxygen levellist": oxygenlevellist})


def prescription(req):
    requestData = req.GET.urlencode()
    requestData = dict(req.GET)
    appointmentId = requestData["appointment"][0]
    prescriptionData = Prescription.objects.get(appointment_id = appointmentId)
    return JsonResponse(model_to_dict(prescriptionData))
