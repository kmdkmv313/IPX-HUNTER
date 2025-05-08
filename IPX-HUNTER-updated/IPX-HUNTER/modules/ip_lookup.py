
import requests
import yaml

def full_lookup(ip):
    result = {}
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)

        data = requests.get(f"https://ipinfo.io/{ip}/json").json()
        result.update(data)

        vpn_key = config.get("vpnapi_key", "")
        if vpn_key:
            vpn_data = requests.get(f"https://vpnapi.io/api/{ip}?key={vpn_key}").json()
            result["vpn"] = vpn_data.get("security", {})
    except Exception as e:
        result["error"] = f"Failed to retrieve data: {str(e)}"
    return result
