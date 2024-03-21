#!/usr/bin/env python

# Script to operte VM on oVirt thru API


import argparse
import requests
import xml.etree.ElementTree as ET

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


def post_api(url: str):
    ovirt_url = url
    username = USERNAME
    password = PASSWORD
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
    username = USERNAME
    password = PASSWORD
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


def main():
    parser = argparse.ArgumentParser(description='Operate oVirt')
    parser.add_argument('--vm_name', required=True)
    parser.add_argument('--action', required=True)
    args = parser.parse_args()
    vm_name = args.vm_name
    action = args.action
    xml_string = get_api(f"{API_URL}/vms")
    root = ET.ElementTree(ET.fromstring(xml_string))
    all_vm = root.findall('vm')
    vid = None
    for v in all_vm:
        if v.find('name').text == vm_name:
            vid = v.get('id')
            
    URL_MAP = {
        "shutdown": f"{API_URL}/vms/{vid}/shutdown",
        "start": f"{API_URL}/vms/{vid}/start",
        "snapshot": f"{API_URL}/vms/{vid}/snapshots"
    }
            
    shutdown_action = post_api(URL_MAP[action])

    print(shutdown_action)

    # shutdown_action = post_api(f"https://manager2.oc.example/ovirt-engine/api/vms/{vid}/start")

    # print(shutdown_action)

    # take_snapshot_action = snapshot_api(f"https://manager2.oc.example/ovirt-engine/api/vms/{vid}/snapshots")
    # print(take_snapshot_action.status_code)
    # print(take_snapshot_action.text)
    
    
if __name__ == "__main__":
    main()