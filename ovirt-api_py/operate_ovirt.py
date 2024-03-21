#!/usr/bin/env python

import argparse
import requests
import xml.etree.ElementTree as ET

from requests.auth import HTTPBasicAuth

vm_name = "ol7a"

def get_api(url: str):
    ovirt_url = url
    username = "admin@internal"
    password = "password"
    headers = {'Content-Type': 'application/xml'} 
    private_url_response_xml = requests.get(
        url=ovirt_url,
        auth=HTTPBasicAuth(username, password),
        verify="ca.pem",
        headers=headers
    )

    # Print xml
    return private_url_response_xml.text


def post_api(url: str):
    ovirt_url = url
    username = "admin@internal"
    password = "password"
    headers = {'Content-Type': 'application/xml'}
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <action/>"""
    private_url_response_xml = requests.post(
        url=ovirt_url,
        auth=HTTPBasicAuth(username, password),
        verify="ca.pem",
        headers=headers,
        data=xml
    )

    # Print xml
    return private_url_response_xml.status_code



def snapshot_api(url: str):
    ovirt_url = url
    username = "admin@internal"
    password = "password"
    headers = {'Content-Type': 'application/xml'}
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <snapshot><description>vm snapshot</description></snapshot>"""
    private_url_response_xml = requests.post(
        url=ovirt_url,
        auth=HTTPBasicAuth(username, password),
        verify="ca.pem",
        headers=headers,
        data=xml
    )

    # Print xml
    return private_url_response_xml

xml_string = get_api("https://manager2.oc.example/ovirt-engine/api/vms")

root = ET.ElementTree(ET.fromstring(xml_string))

all_vm = root.findall('vm')

vid = None

for v in all_vm:
    if v.find('name').text == vm_name:
        vid = v.get('id')
        
# shutdown_action = post_api(f"https://manager2.oc.example/ovirt-engine/api/vms/{vid}/shutdown")

# print(shutdown_action)

# shutdown_action = post_api(f"https://manager2.oc.example/ovirt-engine/api/vms/{vid}/start")

# print(shutdown_action)

take_snapshot_action = snapshot_api(f"https://manager2.oc.example/ovirt-engine/api/vms/{vid}/snapshots")
print(take_snapshot_action.status_code)
print(take_snapshot_action.text)