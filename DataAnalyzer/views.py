from django.shortcuts import render
from django.http import HttpResponse
from DataAnalyzer.models import *
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint

@csrf_exempt
def post_list(request):
    if request.method == "POST":
        humidity = request.POST.get('humidity')
        temperature = request.POST.get('temperature')
    sensor = SensorData(humidity=humidity, temperature=temperature)
    sensor.save()
    print(request.method)
    print(request.body)
    return HttpResponse(humidity,temperature);

def post_model_list(request):
    sensor_data = SensorData.objects.all()
    template='monitor.html'
    context = {
        'sensor_data': sensor_data
    }
    return render(request,template,context)

def get_list_data(request):
    sensor_data = SensorData.objects.all()
    return render(request, 'list_view.html', {'sensor_data': sensor_data})
