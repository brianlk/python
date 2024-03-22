#!/usr/bin/env python

# Script to operte VM on oVirt thru API

import argparse
import json
import os

from auth import Auth
from maps import get_url_xml
from ovirt import oVirtVM


def main():
    if not os.environ.get('OLVM_FQDN'):
        print("Error: environment OLVM_FQDN does not exist.")
        exit()
        
    # Open arguement choices file
    with open("choices.json") as c:
        choices = json.load(c)
    parser = argparse.ArgumentParser(description='Operate oVirt')
    parser.add_argument('--vm_name', required=True)
    parser.add_argument('--action', required=True, choices=choices['actions'])
    args = parser.parse_args()
    vm_name = args.vm_name
    action = args.action
    # Get the oAuth access token
    acces_token = Auth.authenticate()
    v = oVirtVM(vm_name, acces_token)
    vid = v.find_vm()       
    (url, xml) = get_url_xml(vid, action)
    action_result = v.post_api(url, xml)
    print(action_result.status_code)
  
    
if __name__ == "__main__":
    main()