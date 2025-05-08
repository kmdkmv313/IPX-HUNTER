
from modules.ip_lookup import full_lookup
from modules.asn_mapper import get_asn_info
from modules.osint_recon import shodan_lookup
from modules.visualize import map_ip_location

def run(ip):
    print("[*] Performing full lookup...")
    info = full_lookup(ip)
    print(info)

    print("[*] Getting ASN Info...")
    asn = get_asn_info(ip)
    print(asn)

    print("[*] Running Shodan Recon...")
    shodan = shodan_lookup(ip)
    print(shodan)

    print("[*] Mapping location...")
    if "loc" in info:
        map_ip_location(info["loc"], f"results/ip_reports/{ip.replace('.', '_')}.html")
        print(f"[+] Map saved to results/ip_reports/{ip.replace('.', '_')}.html")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    run(target_ip)
