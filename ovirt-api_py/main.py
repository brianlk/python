#!/usr/bin/env python

# Script to operte VM on oVirt thru API


import argparse
import json
import requests
import xml.etree.ElementTree as ET
from auth import Auth
from maps import get_url_xml, API_URL

from requests.auth import HTTPBasicAuth


def get_api(url: str, headers):
    ovirt_url = url
    private_url_response_xml = requests.get(
        url=ovirt_url,
        verify="ca.pem",
        headers=headers
    )

    # Print xml
    return private_url_response_xml.text


def post_api(url: str, xml,  headers):
    ovirt_url = url
    private_url_response_xml = requests.post(
        url=ovirt_url,
        verify="ca.pem",
        headers=headers,
        data=xml
    )

    # Print xml
    return private_url_response_xml


def find_vm(vm_name: str, headers):
    xml_string = get_api(f"{API_URL}/vms", headers)
    root = ET.ElementTree(ET.fromstring(xml_string))
    all_vm = root.findall('vm')
    vid = None
    for v in all_vm:
        if v.find('name').text == vm_name:
            vid = v.get('id')
            return vid
    raise Exception(f"Error: VM {vm_name} not found.")


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

    vid = find_vm(vm_name, headers)         
    
    (url, xml) = get_url_xml(vid, action)
    action_result = post_api(url, xml, headers)

    print(action_result)
  
    
if __name__ == "__main__":
    main()