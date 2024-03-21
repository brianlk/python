#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth


def call_api(object_type: str):
    ovirt_url = f"https://manager2.oc.example/ovirt-engine/api/{object_type}"
    username = "admin@internal"
    password = "password"

    private_url_response_xml = requests.get(
        url=ovirt_url,
        auth=HTTPBasicAuth(username, password),
        verify="ca.pem"
    )

    # Print xml
    return private_url_response_xml.text


x = call_api("datacenters")

print(x)