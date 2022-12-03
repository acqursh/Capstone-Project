import os
from dotenv import load_dotenv
import time as tm
import requests
import jwt
from datetime import datetime, timedelta, time

from twilio.rest import Client

load_dotenv()

start_time = time.min
last_sent = start_time.strftime("%H:%M")
flag = False


def send_alert(content):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=content,
        to='whatsapp:+918826724387'
    )

    print(message.sid)


while True:
    users = requests.get("http://127.0.0.1:7000/users")
    for user in users.json():
        now = datetime.now()
        timestamp = now.strftime("%H:%M")
        decoded = jwt.decode(user['access_token'], 'secret', algorithms=['HS256'])
        access_token = decoded['access_token']
        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {access_token}',
        }
        old_time = now - timedelta(minutes=15)

        old_timestamp = old_time.strftime("%H:%M")
        # print(timestamp, " ", old_timestamp)

        if timestamp <= '00:30':
            old_timestamp = "00:00"

        heart_url = f"https://api.fitbit.com/1/user/{user['user_id']}/activities/heart/date/today/" \
                    f"today/1sec/time/{old_timestamp}/{timestamp}.json"
        heart_response = requests.get(heart_url, headers=headers).json()

        # print(heart_response)

        spo2_url = 'https://api.fitbit.com/1/user/-/spo2/date/today.json'
        spo2_response = requests.get(spo2_url, headers=headers).json()

        spo2 = spo2_response['value']['avg']

        data = heart_response['activities-heart'][0]
        intraday_data = heart_response['activities-heart-intraday']

        restingHR = float(data['value'])
        minHR, maxHR = 65, 65
        for data in intraday_data['dataset']:
            minHR = min(data['value'], minHR)
            maxHR = max(data['value'], maxHR)

        # print(timestamp - last_sent)

        check_time = now - timedelta(minutes=30)
        check_time = check_time.strftime("%H:%M")
        print(check_time, last_sent)
        if check_time == last_sent or not flag:
            if int(restingHR) > 100 and spo2 < 90:
                alert = "Your current readings of Resting Heart Rate and SpO2 are looking abnormal you may want to sit " \
                        "down and take a deep breath. \n" \
                        "If you still feel the same please contact your doctor"
                send_alert(alert)
                last_sent = datetime.now()
                last_sent = last_sent.strftime("%H:%M")
                flag = True

            if maxHR < 100 and minHR > 40:
                alert = "Your heart rates are showing abnormal values, please sit down and take a deep breath. \n" \
                        "If the issue still persists please contact your emergency number"
                send_alert(alert)
                last_sent = datetime.now()
                last_sent = last_sent.strftime("%H:%M")
                flag = True

        print(minHR, maxHR)
    tm.sleep(10)
