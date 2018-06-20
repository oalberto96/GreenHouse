# Client test
import requests
import json


data = data={'humidity': 5.5, 'temperature':79.4}
r = requests.post("http://10.0.0.4:8000/arduinodata", json.dumps(data).encode("utf-8"))
print(r.text)
