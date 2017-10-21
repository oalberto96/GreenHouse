from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arduinodata$', views.post_list, name='post_list'),
    url(r'^sensordata$', views.post_model_list, name='list')
]
