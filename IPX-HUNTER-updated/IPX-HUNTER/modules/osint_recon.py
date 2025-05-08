
import requests
import yaml

def shodan_lookup(ip):
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)

        api_key = config.get("shodan_api_key", "")
        if not api_key:
            return {"error": "Missing Shodan API Key in config.yaml"}

        data = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={api_key}").json()
        return data
    except Exception as e:
        return {"error": f"Shodan API call failed: {str(e)}"}
