from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from UserRegister.models import UserList
import json

# Create your views here.

def user_register(request):
    status = 'Failed'
    message = "User regist success! Please check your e-mail and click the link to varify your e-mail address. Notice that the link only valid within one hour."
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            user_name = json_data['user_name']
            user_password = json_data['user_password']
            user_email = json_data['user_email']
            UserList.objects.create(user_name = user_name,
                    user_password = user_password,
                    user_email = user_email
                )
            status = 'Success'
            user_count = len(UserList.objects.all())
            user_count = str(user_count)
            message = message + "\n There were " + user_count + " users joined."
    except:
        try:
            UserList.objects.get(user_name=user_name)
            message = 'Error: The user name was been used!'
        except:
            message = 'Error: Unknown error occured!'

    return JsonResponse({'status': status, 'message': message })
