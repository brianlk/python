
import xml.etree.ElementTree as ET
import requests

# from auth import Auth
from api_libs.maps import get_api_url


class oVirtVM:
    
    def __init__(self, vm_name, acces_token):
        self.vm_name = vm_name
        self.auth_headers = {
            'Authorization': f"Bearer {acces_token}",
            'Content-Type': 'application/xml',
            'Accept': 'application/xml'
            }
        
        
    def find_vm(self):
        xml_string = self.get_api(f"{get_api_url()}/vms")
        root = ET.ElementTree(ET.fromstring(xml_string.text))
        all_vm = root.findall('vm')
        vid = None
        for v in all_vm:
            if v.find('name').text == self.vm_name:
                vid = v.get('id')
                return vid
        if not vid:
            raise Exception(f"Error: VM {self.vm_name} not found.")
    
    
    def get_api(self, url: str):
        ovirt_url = url
        private_url_response_xml = requests.get(
            url=ovirt_url,
            verify="ca.pem",
            headers=self.auth_headers,
            params={
                "search": f"name={self.vm_name}", # url encode is done by python library
                "case_sensitive": "true"
                }
            )

        # TODO
        # if private_url_response_xml.status_code == 401:
        #     Auth.refresh_token()
        # Print xml
        return private_url_response_xml
    
    
    def post_api(self, url: str, xml):
        ovirt_url = url
        private_url_response_xml = requests.post(
            url=ovirt_url,
            verify="ca.pem",
            headers=self.auth_headers,
            data=xml
            )

        # Print xml
        return private_url_response_xml
    
