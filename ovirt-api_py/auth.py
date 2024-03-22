import json
import requests
import os.path


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
            j = json.loads(oauth_output.text)
            token = j['access_token']
            Auth._access_token_save(token)
            print(j)
            
        return token
    
    @staticmethod
    def _access_token_check():
        if os.path.isfile(FILE_PATH):
            with open(FILE_PATH) as f:
                return f.readline()
        
        return None
            
    @staticmethod
    def _access_token_save(token: str):
        with open(FILE_PATH, 'w') as f:
            f.write(token)