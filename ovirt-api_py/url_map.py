
API_URL = "https://manager2.oc.example/ovirt-engine/api"

def get_url_params(vid, action):
    url_map = {
        "shutdown": f"{API_URL}/vms/{vid}/shutdown",
        "start": f"{API_URL}/vms/{vid}/start",
        "snapshot": f"{API_URL}/vms/{vid}/snapshots"
    }
    
    return url_map[action]