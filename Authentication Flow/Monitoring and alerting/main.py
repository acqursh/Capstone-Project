import requests
import jwt

users = requests.get("http://127.0.0.1:7000/users")
for user in users.json():
    print(user)
    decoded = jwt.decode(user['access_token'], 'secret', algorithms=['HS256'])
    access_token = decoded['access_token']
    headers = {
        'accept': 'application/json',
        'authorization': f'Bearer {access_token}',
    }

    url = f"https://api.fitbit.com/1/user/{user['user_id']}/activities/heart/date/today/today/1min/time/15:00/15:05.json"
    r = requests.get(url, headers=headers)
    print(r.json())
