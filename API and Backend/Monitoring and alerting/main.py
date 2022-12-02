import time

import requests
import jwt
from datetime import datetime, timedelta

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
        print(timestamp)

        url = f"https://api.fitbit.com/1/user/{user['user_id']}/activities/heart/date/today/today/1sec/time/00:00/{timestamp}.json"
        r = requests.get(url, headers=headers).json()
        intraday_data = r['activities-heart-intraday']
        print(intraday_data)
        for data in intraday_data['dataset']:

            print(data['value'], data['time'])
    time.sleep(10)
