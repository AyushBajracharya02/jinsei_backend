from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from my_models.models import AppUser, Doctor, nameRegex, passwordRegex, phoneRegex
import re
from django.forms.models import model_to_dict

def validateSignUp(data):
    errors = {}
    if not re.match(nameRegex, data["firstname"]):
        errors[
            "name"
        ] = "Name should only contain letters and should be 2-32 characters"
    elif not re.match(nameRegex, data["lastname"]):
        errors[
            "name"
        ] = "Name should only contain letters and should be 2-32 characters"
    if not re.match(phoneRegex, data["phonenumber"]):
        errors[
            "phone"
        ] = "Phone should only contain numbers and should be 10 characters"
    if not re.match(passwordRegex, data["password"]):
        errors["password"] = "Password should be between 8 and 32 characters"
    return errors


@csrf_exempt
def signup(request):
    if request.method == "POST":
        signup_data = request.body.decode("utf-8")
        signup_data = json.loads(signup_data)
        errors = validateSignUp(signup_data)
        if errors != {}:
            return JsonResponse({"access": False, "errors": errors})
        if signup_data["accounttype"] == "Patient":
            user = AppUser(
                firstname=signup_data["firstname"],
                lastname=signup_data["lastname"],
                password=signup_data["password"],
                phonenumber=signup_data["phonenumber"],
            )
            try:
                user.save()
                user = model_to_dict(user)
                user.update({"isdoctor":False})
                return JsonResponse({"access": True, "userdata": user})
            except Exception as e:
                print("Error while saving user:", e)
                return JsonResponse({"access": False})
        if signup_data["accounttype"] == "Doctor":
            doctor = Doctor(
                firstname=signup_data["firstname"],
                lastname=signup_data["lastname"],
                password=signup_data["password"],
                phonenumber=signup_data["phonenumber"],
            )
            try:
                doctor.save()
                doctor = model_to_dict(doctor)
                doctor.update({"isdoctor":True})
                return JsonResponse({"access": True, "userdata": doctor})
            except Exception as e:
                print("Error while saving user:", e)
                return JsonResponse({"access": False})
