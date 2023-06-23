from django.http import JsonResponse
from my_models.models import Doctor
from django.forms.models import model_to_dict
from django.http import QueryDict
import json


def doctors(request):
    doctors = Doctor.objects.filter(price__isnull=False, schedule__isnull=False)
    alldoctors = [model_to_dict(doctor) for doctor in doctors]
    return JsonResponse({"doctors": alldoctors})


def doctor(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    doctor = Doctor.objects.get(id = requestData['doctorid'])
    return JsonResponse(model_to_dict(doctor))

def doctorTimeScheduleForDay(request):
    requestData = request.GET.urlencode()
    requestData = QueryDict(requestData)
    day = requestData['day']
    doctorData = json.loads(doctor(request).content)
    return JsonResponse(doctorData['schedule'][day])