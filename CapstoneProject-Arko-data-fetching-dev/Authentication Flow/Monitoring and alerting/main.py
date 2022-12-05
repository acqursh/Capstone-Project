import requests
import jwt

users = requests.get("http://127.0.0.1:7000/users")
for user in users.json():
    decoded = jwt.decode(user['access_token'], 'secret', algorithms=['HS256'])
    access_token = decoded['access_token']
    headers = {
        'accept': 'application/json',
        'authorization': f'Bearer {access_token}',
    }
    url = f"https://api.fitbit.com/1/user/{user.user_id}/activities/heart/date/2022-11-09/1d.json"
    print(user['email_id'], access_token)
