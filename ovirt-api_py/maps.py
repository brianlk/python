
API_URL = "https://manager2.oc.example/ovirt-engine/api"
XML_HEADER = "<?xml version='1.0' encoding='utf-8'?>"

def get_url_xml(vid, action):
    url_map = {
        "shutdown": f"{API_URL}/vms/{vid}/shutdown",
        "start": f"{API_URL}/vms/{vid}/start",
        "snapshot": f"{API_URL}/vms/{vid}/snapshots",
        "poweroff": f"{API_URL}/vms/{vid}/stop",
    }
    
    xml_map = {
        "shutdown": f"{XML_HEADER}<action/>",
        "start": f"{XML_HEADER}<action/>",
        "snapshot": f"{XML_HEADER}<snapshot><description>vm snapshot</description></snapshot>",
        "poweroff": f"{XML_HEADER}<action/>",
    }
    
    return url_map[action], xml_map[action]
