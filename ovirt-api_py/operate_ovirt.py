#!/usr/bin/env python

# Script to operte VM on oVirt thru API


import argparse
import json
import requests
import xml.etree.ElementTree as ET
from auth import Auth
from url_map import get_url_params

from requests.auth import HTTPBasicAuth

USERNAME = "admin@internal"
PASSWORD = "password"
API_URL = "https://manager2.oc.example/ovirt-engine/api"


def get_api(url: str):
    ovirt_url = url
    username = USERNAME
    password = PASSWORD
    headers = {'Content-Type': 'application/xml'} 
    private_url_response_xml = requests.get(
        url=ovirt_url,
        auth=HTTPBasicAuth(username, password),
        verify="ca.pem",
        headers=headers
    )

    # Print xml
    return private_url_response_xml.text


def post_api(url: str, headers):
    ovirt_url = url
    xml = """<?xml version='1.0' encoding='utf-8'?><action/>"""
    private_url_response_xml = requests.post(
        url=ovirt_url,
        verify="ca.pem",
        headers=headers,
        data=xml
    )

    # Print xml
    return private_url_response_xml.status_code



def snapshot_api(url: str, headers):
    ovirt_url = url
    xml = """<?xml version='1.0' encoding='utf-8'?><snapshot><description>vm snapshot</description></snapshot>"""
    private_url_response_xml = requests.post(
        url=ovirt_url,
        verify="ca.pem",
        headers=headers,
        data=xml
    )

    # Print xml
    return private_url_response_xml


def find_vm(vm_name: str):
    xml_string = get_api(f"{API_URL}/vms")
    root = ET.ElementTree(ET.fromstring(xml_string))
    all_vm = root.findall('vm')
    vid = None
    for v in all_vm:
        if v.find('name').text == vm_name:
            vid = v.get('id')
            return vid


def main():
    parser = argparse.ArgumentParser(description='Operate oVirt')
    parser.add_argument('--vm_name', required=True)
    parser.add_argument('--action', required=True)
    args = parser.parse_args()
    vm_name = args.vm_name
    action = args.action
    
    
    acces_token = Auth.authenticate()
    headers = {
        'Authorization': f"Bearer {acces_token}",
        'Content-Type': 'application/xml'
    }

    vid = find_vm(vm_name)         
    
    shutdown_action = snapshot_api(get_url_params(vid, action), headers)

    print(shutdown_action)
  
    
if __name__ == "__main__":
    main()