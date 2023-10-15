from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from my_models.models import AppUser, Doctor, nameRegex, passwordRegex, phoneRegex
import json
import re
from datetime import datetime


def validateUpdate(data):
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
def updateuser(request):
    if request.method == "POST":
        update_data = request.body.decode("utf-8")
        update_data = json.loads(update_data)
        errors = validateUpdate(update_data)
        if errors != {}:
            return JsonResponse({"status": False, "errors": errors})
        if not update_data["isdoctor"]:
            user = AppUser.objects.get(id=update_data["id"])
            for fieldName, value in model_to_dict(user).items():
                if fieldName == "age" or fieldName == "sex":
                    continue
                if fieldName == "date_of_birth":
                    if update_data["date_of_birth"] == "null":
                        continue
                    update_data["date_of_birth"] = datetime.strptime(
                        update_data["date_of_birth"], "%Y-%m-%d"
                    ).date()
                setattr(user, fieldName, update_data[fieldName])
            user.save()
            return JsonResponse({"status": True})
        user = Doctor.objects.get(id=update_data["id"])
        for fieldName, value in model_to_dict(user).items():
            if fieldName == "age" or fieldName == "sex":
                continue
            if fieldName == "date_of_birth":
                if update_data["date_of_birth"] == "null":
                    continue
                update_data["date_of_birth"] = datetime.strptime(
                    update_data["date_of_birth"], "%Y-%m-%d"
                ).date()
            setattr(user, fieldName, update_data[fieldName])
        user.save()
        return JsonResponse({"status": True})
