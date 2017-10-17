from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_list(request):
    if request.method == "POST":
        r = request.POST['number']
    return HttpResponse(r);
