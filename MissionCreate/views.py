from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from MissionCreate.models import ShortermMissionList

import datetime
import json

# Create your views here.

def register_short_mission(request):
    status = 'failed'
    message = 'Shorterm mission created !'
    shorterm_mission_count = 0
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            name = json_data['name']
            # check if mission have been created
            #nameList = ShortermMissionList.objects.all()
            #for i in range (len(nameList)-1):
            #    if nameList[i] == name:
            #        error_message = "The mission have been created !"
            #        text = error_message
            #        return JsonResponse({'status': result, 'message': error_message})
            #        break
            # Null value
            emergency_level = int(json_data['emergency_level'])
            important_level = int(json_data['important_level'])
            try:
                related_link_1 = json_data['related_link_1']
            except:
                related_link_1 = "127.0.0.1"

            try:
                related_link_2 = json_data['related_link_2']
            except:
                related_link_2 = "127.0.0.1"

            try:
                assign_time = json_data['assign_time']
            except:
                assign_time = datetime.date.today()
            try:
                launch_time = json_date['launch_time']
            except:
                launch_time = datetime.date.today()

            ShortermMissionList.objects.create(name = name, 
                    assign_time = assign_time,
                    launch_time = launch_time,
                    expected_finish_time = json_data['expected_finish_time'],
                    emergency_level = json_data['emergency_level'],
                    important_level = json_data['important_level'],
                    detail = json_data['discription'],
                    related_link_1 = related_link_1,
                    related_link_2 = related_link_2
                )
        status = "Success"
        shorterm_mission_count = len(ShortermMissionList.objects.all())
    except:
        try:
            ShortermMissionList.objects.get(name=name)
            message = "Created failed, the same shorterm mission is available!"
        except:
            message = "Created failed, check out the following required field: name, expected_finish_time, emergency_level, important_level"
        #try:
        #    if (ShortermMissionList.objects.get(name = name) != None):
        #        message = "The mission have been created! "
        #except:
        #    message = "Create failed, unknown error"
    return JsonResponse({'status': status, 'message': message, 'exist shorterm mission': shorterm_mission_count})
