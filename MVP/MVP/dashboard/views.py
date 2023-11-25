from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import os
import sys
from .modules.moduleA import *
from .modules.moduleB import *


def dashboard(request):
    return render(request, "dashboard.html")

@ensure_csrf_cookie
def uploaddatacheck(request):
    global f
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        for f in files:
            handle_uploaded_file(f)

        mainModuleA(f.name)
        return JsonResponse(
            {'msg': f'Языковая модель успешно обучена с помощью DataSet: {f.name}<br>Можно приступать к работе.'})

@ensure_csrf_cookie
def uploadreles(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        # print(files)
        for f in files:
            handle_uploaded_file(f)
        metric=mainModuleB(f.name)
        return JsonResponse(
            {'msg': 'По вашем данным: '+f.name+' был сформирован ответ<br><a href="../static/output.csv" download>Скачать</a><br>Метрика результата: '+metric})

def handle_uploaded_file(f):
    if not os.path.exists("dashboard/modules/file/"):
        os.mkdir('dashboard/modules/file/')
    with open(f"dashboard/modules/file/{f.name}", "wb") as destination:
        for chunk in f.chunks():
            destination.write(chunk)