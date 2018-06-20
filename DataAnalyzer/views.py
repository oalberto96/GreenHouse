from django.shortcuts import render
from django.http import HttpResponse
from DataAnalyzer.models import *
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.http import JsonResponse
import json

@csrf_exempt
def post_list(request):
    print(request.method)
    print(request.body)
    if request.method == "POST":
        json_data = json.loads(request.body.decode("utf-8"))
        if json_data:
            humidity = json_data['humidity']
            temperature = json_data['temperature']
        else:
            humidity = request.POST.get('humidity')
            temperature = request.POST.get('temperature')
            print(humidity)
            print(temperature)
    sensor = SensorData(humidity=humidity, temperature=temperature)
    sensor.save()

    return HttpResponse(humidity,temperature);

def post_model_list(request):
    sensor_data = SensorData.objects.all().order_by('-date')
    actuators = get_actuators(sensor_data)
    template='monitor.html'
    context = {
        'sensor_data': sensor_data
    }
    context.update(actuators)
    return render(request,template,context)

def get_list_data(request):
    sensor_data = SensorData.objects.all().order_by('-date')
    actuators = get_actuators(sensor_data)
    context = {
        'sensor_data': sensor_data
    }
    context.update(actuators)
    return render(request, 'list_view.html',context)

def get_actuators_status_android(request):
    sensor_data = SensorData.objects.all().order_by('-date')
    return JsonResponse(get_actuators(sensor_data))


def get_actuators(query):
    actuators = {}
    if not query:
        actuators['fan'] = "Desactivado"
        actuators['light'] = "Desactivado"
        actuators['water'] = "Desactivado"
    else:
        latest = query[0]
        if latest.temperature < 25:
            actuators['fan'] = "Desactivado"
            actuators['light'] = "Activado"
        else:
            if latest.temperature>=25 and latest.temperature <=30:
                actuators['fan'] = "Desactivado"
                actuators['light'] = "Desactivado"
            elif latest.temperature > 30:
                actuators['fan'] = "Desactivado"
                actuators['light'] = "Desactivado"
        if latest.humidity < 60:
            actuators['water'] = "Activado"
        else:
            actuators['water'] = "Desactivado"
    return actuators
