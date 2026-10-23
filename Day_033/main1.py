import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "somtochukwu@gmail.com"
PASSWORD = "1234"

MY_LAT = 51.507351
MY_LNG = 40.127758

def is_iss_overheard():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT <= iss_latitude <=MY_LAT+5 and MY_LNG == iss_longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }


    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"])
    sunset = int(data["results"]["sunset"])


    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overheard() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up☝️\n\nThe iss is above you in the sky"
        )
