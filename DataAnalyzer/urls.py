from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arduinodata$', views.post_list, name='post_request'),
    url(r'^sensordata$', views.post_model_list, name='sensor_monitor'),
    url(r'^refresh_list/$', views.get_list_data, name='list_view')
]
