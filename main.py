import base64
import json
import sys
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

import keyboard
import requests

client_id = "238R4F"
client_secret = "3a556b63e50ee80ad4469a1615e7b623"


def make_request():
    url = f"https://www.fitbit.com/oauth2/authorize?response_type=code&client_id={client_id}&" \
          "redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Flogin&scope=activity%20heartrate" \
          "%20location%20nutrition%20profile%20settings%20sleep%20social%20weight%20" \
          "oxygen_saturation%20respiratory_rate%20temperature&expires_in=604800"

    webbrowser.open(url, new=1, autoraise=True)


def wait_for_response(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    buffer = 1
    sys.stderr = open(r'.\logfile.txt', 'w',
                      buffer)
    return httpd.handle_request()


def read_log():
    with open("logfile.txt", "r") as file:
        for line in file:
            pass
        last_line = line
    return last_line[54:-16]


def close_tab():
    keyboard.press_and_release('ctrl+w')
    time.sleep(0.2)
    keyboard.press_and_release('alt+tab')


def get_token():
    token = f"{client_id}:{client_secret}"
    auth_token = str(base64.b64encode(token.encode("ascii")))
    headers = {
        'Authorization': f'Basic {auth_token[2:-1]}',
    }
    code = read_log()

    data = {
        'clientId': f'{client_id}',
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:8080/login',
        'code': f'{code[:-1]}',
    }

    response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)
    token = json.dumps(response.json(), indent=4)

    with open("token.json", "w") as file:
        file.write(token)


def restore_token(refresh_token):
    token = f"{client_id}:{client_secret}"
    auth_token = str(base64.b64encode(token.encode("ascii")))
    headers = {
        'accept': 'application/json',
        'authorization': f'Basic {auth_token[2:-1]}',
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = f'grant_type=refresh_token&refresh_token={refresh_token}'

    response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)

    token = json.dumps(response.json(), indent=4)

    with open("token.json", "w") as file:
        file.write(token)


def get_user(access_token):
    headers = {
        'accept': 'application/json',
        'authorization': f'Bearer {access_token}',
    }

    response = requests.get('https://api.fitbit.com/1/user/-/profile.json', headers=headers)
    user_info = response.json()
    d = {}
    lst = ["age", "firstName", "lastName", "gender", "weight"]
    for i in user_info['user']:
        if i in lst:
            d[i] = user_info['user'][i]

    print(d)


if __name__ == '__main__':
    try:
        with open("token.json", "r") as f:
            json_obj = json.load(f)
        get_user(json_obj['access_token'])
        # restore_token(json_obj['refresh_token'])
    except:
        make_request()
        wait_for_response()
        close_tab()
        time.sleep(2)
        get_token()
# read_log()
