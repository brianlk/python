
API_URL = "https://manager2.oc.example/ovirt-engine/api"

def get_url_xml(vid, action):
    url_map = {
        "shutdown": f"{API_URL}/vms/{vid}/shutdown",
        "start": f"{API_URL}/vms/{vid}/start",
        "snapshot": f"{API_URL}/vms/{vid}/snapshots"
    }
    
    xml_map = {
        "shutdown": """<?xml version='1.0' encoding='utf-8'?><action/>""",
        "start": """<?xml version='1.0' encoding='utf-8'?><action/>""",
        "snapshot": """<?xml version='1.0' encoding='utf-8'?><snapshot><description>vm snapshot</description></snapshot>"""
    }
    
    return url_map[action], xml_map[action]
