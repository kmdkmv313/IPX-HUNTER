
import folium

def map_ip_location(location_str, output_file):
    try:
        lat, lon = map(float, location_str.split(","))
        m = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], popup="Target IP").add_to(m)
        m.save(output_file)
    except:
        print("[-] Failed to generate map.")
