# Client test
import requests
r = requests.post("http://10.0.0.8:8000/arduinodata", data={'humidity': 5, 'temperature':79})
print(r.text)
