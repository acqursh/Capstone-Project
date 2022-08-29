import base64
import sys
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

import keyboard
import pkce
import requests

client_id = "238R4F"
client_secret = "3a556b63e50ee80ad4469a1615e7b623"


def make_request():
    code_verifier = pkce.generate_code_verifier(length=128)
    code_challenge = pkce.get_code_challenge(code_verifier)

    url = f"https://www.fitbit.com/oauth2/authorize?client_id={client_id}&response_type=code" \
          f"&code_challenge={code_challenge}&code_challenge_method=S256" \
          f"&scope=activity%20heartrate%20location%20nutrition%20oxygen_saturation%20profile" \
          f"%20respiratory_rate%20settings%20sleep%20social%20temperature%20weight"

    webbrowser.open(url, new=1, autoraise=True)


def wait_for_response(server_class=HTTPServer,
                      handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    buffer = 1
    sys.stderr = open(r'C:\Users\arkop\OneDrive\Desktop\College Stuff\Capstone\logfile.txt', 'w', buffer)
    return httpd.handle_request()


def read_log():
    with open("logfile.txt", "r") as f:
        for line in f:
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
    print(auth_token[2:-1])
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
    print(response.text)


if __name__ == '__main__':
    make_request()
    wait_for_response()
    close_tab()
    time.sleep(2)
    get_token()
    # read_log()
