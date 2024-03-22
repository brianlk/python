import json
import requests
import os.path


class Auth:
    
    @staticmethod
    def authentication():
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
            }
    
        params = {
            "grant_type": "password",
            "scope": "ovirt-app-api",
            "username": "admin@internal",
            "password": "password"
        }
        oauth_output = requests.post(
            url='https://manager2.oc.example/ovirt-engine/sso/oauth/token',
            params=params,
            verify="ca.pem",
            headers=headers
        )
        j = json.loads(oauth_output.text)
        token = j['access_token']
        
        return token