from django.shortcuts import render
from django.http import HttpResponse
from DataAnalyzer.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_list(request):
    if request.method == "POST":
        humidity = request.POST['humidity']
        temperature = request.POST['temperature']
    sensor = SensorData(humidity=humidity, temperature=temperature)
    sensor.save()

    return HttpResponse(humidity,temperature);

def post_model_list(request):
    qs = SensorData.objects.all()
    print(qs)
    templates="list_view.html"
    context = {
        'object_list': qs
    }
    return render(request,templates,context)
