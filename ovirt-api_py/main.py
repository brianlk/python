#!/usr/bin/env python

# Script to operte VM on oVirt thru API

import argparse
import json
import os

from api_libs.auth import Auth
from api_libs.maps import get_url_xml
from api_libs.ovirt import oVirtVM


def check_args():
    # Open arguement choices file
    with open("choices.json") as c:
        choices = json.load(c)
    parser = argparse.ArgumentParser(description='Operate oVirt')
    parser.add_argument('--vm_name', required=True)
    parser.add_argument('--action', required=True, choices=choices['actions'])
    parser.add_argument('--debug', required=False)

    return parser.parse_args()


def main():
    if not os.environ.get('OLVM_FQDN'):
        print("Error: environment OLVM_FQDN does not exist.")
        exit()
        
    args = check_args()
    vm_name = args.vm_name
    action = args.action
    # Get the oAuth access token
    acces_token = Auth.authenticate()
    v = oVirtVM(vm_name, acces_token)
    vid = v.find_vm()       
    (url, xml) = get_url_xml(vid, action)
    action_result = v.post_api(url, xml)
    print(f"http status code: {action_result.status_code}")
    if args.debug:
        print(action_result.text)
  
    
if __name__ == "__main__":
    main()
