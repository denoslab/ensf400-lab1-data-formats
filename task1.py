 
import json
 
# Load the JSON data
with open('interface-data.json') as file:
    json_data = json.load(file)
 
# Print header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<12} {'Speed':<7} {'MTU':<6}")
print("-" * 80)
 
# Iterate and extract relevant data
for interface in json_data["imdata"]:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {descr:<12} {speed:<7} {mtu:<6}")
 
