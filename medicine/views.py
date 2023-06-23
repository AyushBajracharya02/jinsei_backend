from django.shortcuts import render
from django.http import JsonResponse
from my_models.models import Medicine, Prescription, Appointment, AppUser, Doctor
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json
from django.contrib.contenttypes.models import ContentType
from datetime import date


def medicinelist(request):
    medicines = Medicine.objects.filter()
    medicinelist = [model_to_dict(medicine) for medicine in medicines]
    return JsonResponse({"medicines": medicinelist})


@csrf_exempt
def addPrescription(request):
    if request.method == "POST":
        newprescription = request.body.decode("utf-8")
        newprescription = json.loads(newprescription)
        prescription = Prescription(
            appointment=Appointment.objects.get(id=newprescription["appointment"]),
            weight=newprescription["weight"],
            temperature=newprescription["temperature"],
            pulse_rate=newprescription["pulserate"],
            blood_pressure=[
                newprescription["bloodpressure"]["upper"],
                newprescription["bloodpressure"]["lower"],
            ],
            oxygen_level=newprescription["oxygenlevel"],
            medication=newprescription["schedules"],
            createddate = date.today()
        )
        prescription.save()
        return JsonResponse({"Hello": "World"})


def medication(request):
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
    # print([appointment for appointment in appointments])
    medications = []
    for appointment in appointments:
        # print(appointment.prescription_set)
        medications.append(appointment.prescription_set.first())
    medications = [model_to_dict(medication) for medication in medications]
    medicationsreturn = []
    for medication in medications:
        medicationsreturn.append({key:medication[key] for key in ['id','appointment','medication']})
    return JsonResponse({"medications": medicationsreturn})
