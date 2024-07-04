import requests

mydata={'nama':'hakim'}
req=requests.post("http://127.0.0.1:5000/cobarequest", data=mydata)

print(req.text)
