#!/usr/bin/env python

# Script to operte VM on oVirt thru API

import argparse

from auth import Auth
from maps import get_url_xml
from ovirt import oVirt


def main():
    parser = argparse.ArgumentParser(description='Operate oVirt')
    parser.add_argument('--vm_name', required=True)
    parser.add_argument('--action', required=True)
    args = parser.parse_args()
    vm_name = args.vm_name
    action = args.action
    
    acces_token = Auth.authenticate()
    v = oVirt(vm_name, acces_token)
    vid = v.find_vm()       
    (url, xml) = get_url_xml(vid, action)
    action_result = v.post_api(url, xml)
    print(action_result)
  
    
if __name__ == "__main__":
    main()