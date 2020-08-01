from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from celery import current_app
from wedding.models import OurStory
import json
from django.views.decorators.csrf import csrf_exempt
from .tasks import ExecGoogleDirectionTask


def home(request):
    return render(request, 'home.html', context={
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'timelineEventSet': OurStory().StoryEvents
    })


@csrf_exempt
def asyncGoogleDirectionTask(request):
    if request.method == "POST":  # 如果是以POST的方式才處理
        # 取得表單輸入資料
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        departure = received_json_data['Departure']
        destination = "嘉義市秀泰影城"
        mode = received_json_data['Mode']
        task = ExecGoogleDirectionTask.delay(departure, destination, mode)
        print("task:{}".format(task))
        result = {
            "task_id": task.id,
            "task_status": task.status
        }
        return JsonResponse(data=result, status=200)


@csrf_exempt
def getResult(request, task_id):
    if request.method == "GET":  # 如果是以POST的方式才處理
        print(task_id)
        task = current_app.AsyncResult(task_id)
        print("task:{}".format(task))
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            result = task.get()
            response_data['results'] = result
        return JsonResponse(data=response_data, status=200)
