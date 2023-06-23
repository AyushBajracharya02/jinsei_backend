from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from my_models.models import AppUser
import json

@csrf_exempt
def updateuser(request):
    if request.method == "POST":
        update_data = request.body.decode("utf-8")
        update_data = json.loads(update_data)
        # errors = validateUpdate(update_data)
        # if errors != {}:
        #     return JsonResponse({"access": False, "errors": errors})
        if not update_data['isdoctor']:
            user = AppUser.objects.get(id = update_data['id'])
            for key,value in update_data:
                print ('%s %s'.format(key,value))
