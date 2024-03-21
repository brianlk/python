#!/usr/bin/env python

import requests
import xml.etree.ElementTree as ET

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


xml_string = call_api("vms")

root = ET.ElementTree(ET.fromstring(xml_string))

xxx = root.findall('vm')

print(xxx[0].find('name').text)