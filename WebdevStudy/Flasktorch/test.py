
import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('./kitten.jpg','rb')})
print(resp.json())