
import os


XML_HEADER = "<?xml version='1.0' encoding='utf-8'?>"


def get_url_xml(vid, action):
    api_url = get_api_url()
    url_map = {
        "shutdown": f"{api_url}/vms/{vid}/shutdown",
        "start": f"{api_url}/vms/{vid}/start",
        "snapshot": f"{api_url}/vms/{vid}/snapshots",
        "poweroff": f"{api_url}/vms/{vid}/stop",
        "suspend": f"{api_url}/vms/{vid}/suspend",
    }
    
    xml_map = {
        "shutdown": f"{XML_HEADER}<action/>",
        "start": f"{XML_HEADER}<action/>",
        "snapshot": f"{XML_HEADER}<snapshot><description>vm snapshot</description></snapshot>",
        "poweroff": f"{XML_HEADER}<action><force>true</force></action>",
        "suspend": f"{XML_HEADER}<action/>",
    }
    
    return url_map[action], xml_map[action]


def get_api_url():
    return f"https://{os.environ.get('MANAGER_FQDN')}/ovirt-engine/api"
