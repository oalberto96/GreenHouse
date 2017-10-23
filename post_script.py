# Client test
import requests
r = requests.post("http://10.0.0.2:8000/arduinodata", data={'humidity': 5.5, 'temperature':79.4})
print(r.text)
