import json
import requests
import os.path
import time


FILE_PATH = '/tmp/access_token.ovirt'

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

PARAMS = {
    "grant_type": "password",
    "scope": "ovirt-app-api",
    "username": "admin@internal",
    "password": "password"
}

OAUTH_URL = 'https://manager2.oc.example/ovirt-engine/sso/oauth/token'

class Auth:
    
    @staticmethod
    def authenticate():
        token = Auth._access_token_check()
        if not token:
            oauth_output = requests.post(
                url=OAUTH_URL,
                params=PARAMS,
                verify="ca.pem",
                headers=HEADERS
            )
            Auth._access_token_save(oauth_output.text)
            x = json.loads(oauth_output.text)
            token = x["access_token"]
            
        return token
    
    @staticmethod
    def _access_token_check():
        token = None
        if os.path.isfile(FILE_PATH):
            with open(FILE_PATH) as f:
                token = f.readline()
            d = json.loads(token)
            json_expiry_time = int(d["exp"]) / 1000
            # Check if the access token is expired
            delta = json_expiry_time - int(time.time())
            if delta < 0:
                return None
            token = d["access_token"]
         
        return token
            
    @staticmethod
    def _access_token_save(token: str):
        with open(FILE_PATH, 'w') as f:
            f.write(token)