
import requests

def get_asn_info(ip):
    try:
        data = requests.get(f"https://api.bgpview.io/ip/{ip}").json()
        return data.get("data", {}).get("prefixes", [])
    except:
        return []
