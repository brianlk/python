
import json
import os
import requests
import os.path
import time


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


class Auth:
    
    file_path = f"/tmp/access_token_{os.environ.get('OLVM_FQDN')}.ovirt"
    oAuth_URL = f"https://{os.environ.get('OLVM_FQDN')}/ovirt-engine/sso/oauth/token"
    
    
    @staticmethod
    def authenticate():
        token = Auth._access_token_check()
        if not token:
            oauth_output = requests.post(
                url=Auth.oAuth_URL,
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
        if os.path.isfile(Auth.file_path):
            with open(Auth.file_path) as f:
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
        with open(Auth.file_path, 'w') as f:
            f.write(token)