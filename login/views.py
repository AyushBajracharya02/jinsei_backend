from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from my_models.models import AppUser, Doctor, phoneRegex, passwordRegex
from django.forms.models import model_to_dict
import re


def validateLogin(data):
    errors = {}
    if not re.match(phoneRegex, data["phonenumber"]):
        errors[
            "phone"
        ] = "Phone should only contain numbers and should be 10 characters"
    if not re.match(passwordRegex, data["password"]):
        errors["password"] = "Password should be between 8 and 32 characters"
    return errors


@csrf_exempt
def login(request):
    if request.method == "POST":
        login_data = request.body.decode("utf-8")
        login_data = json.loads(login_data)
        errors = validateLogin(login_data)
        if errors != {}:
            return JsonResponse({"access": False, "errors": errors})
        if login_data["accounttype"] == "Patient":
            try:
                user = AppUser.objects.get(
                    phonenumber=login_data["phonenumber"],
                    password=login_data["password"],
                )
                user = model_to_dict(user)
                user.update({"isdoctor":False})
                return JsonResponse({"access": True, "userdata": user})
            except AppUser.DoesNotExist:
                return JsonResponse({"access": False})
        if login_data["accounttype"] == "Doctor":
            try:
                user = Doctor.objects.get(
                    phonenumber=login_data["phonenumber"],
                    password=login_data["password"],
                )
                user = model_to_dict(user)
                user.update({"isdoctor":True})
                return JsonResponse({"access": True, "userdata": user})
            except AppUser.DoesNotExist:
                return JsonResponse({"access": False})
