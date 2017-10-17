# Client test
import requests
r = requests.post("http://10.0.0.2:8000/arduinodata", data={'number': 5})
print(r.text)
