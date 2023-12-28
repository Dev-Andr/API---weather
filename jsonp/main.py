import requests
import smtplib, pandas
from datetime import datetime

smtplib.SMTP('smtp.gmail.com', port=587)
mymail = 'aditesseracat@gmail.com'
pwd = 'lirl htyj hqzv hlxg'

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
res = response.json()
lo = res["iss_position"]["longitude"]
la = res["iss_position"]["latitude"]

para = {
    'lat': 40.785091,
    'lng': -73.968285,
    'formatted': 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=para)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")
sunset = data["results"]["sunset"].split("T")
sunrise[1].split("+")
sunset[1].split("+")

now = datetime.now()

def send(i,txt):
    with smtplib.SMTP('smtp.gmail.com')as cnc:
        cnc.starttls()
        cnc.login(user=mymail,password=pwd)
        cnc.sendmail(
            from_addr=mymail,
            to_addrs=i,
            msg=f"Subject:Birthday Birthday Birthday{txt}"
        )


if lo == para[0] and la == para[1]:
    send("aaditsingal7859@gmail.com","Look Above!")