# import json
# import requests
# import time

# INPUT_FILE = "homes.json"  # Your original fixtures
# OUTPUT_FILE = "homes_with_coords.json"

# def geocode_address(address):
#     """Query OpenStreetMap Nominatim to get latitude and longitude."""
#     url = "https://nominatim.openstreetmap.org/search"
#     params = {
#         "q": address + ", Nashville, TN",  # make sure it's scoped to Nashville
#         "format": "json",
#         "addressdetails": 0,
#         "limit": 1
#     }
#     headers = {"User-Agent": "NashvilleHomesMapper/1.0 (your_email@example.com)"}
#     response = requests.get(url, params=params, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             return float(data[0]["lat"]), float(data[0]["lon"])
#     return None, None

# def main():
#     with open(INPUT_FILE, "r") as f:
#         homes = json.load(f)

#     for home in homes:
#         address = home["fields"]["address"]
#         lat, lng = geocode_address(address)
#         if lat and lng:
#             home["fields"]["lat"] = lat
#             home["fields"]["lng"] = lng
#             print(f"✓ Geocoded: {address} → ({lat}, {lng})")
#         else:
#             print(f"✗ Could not geocode: {address}")
#         time.sleep(1)  # respect Nominatim usage policy

#     with open(OUTPUT_FILE, "w") as f:
#         json.dump(homes, f, indent=2)

#     print(f"\n✅ Done! Updated file saved as {OUTPUT_FILE}")

# if __name__ == "__main__":
#     main()
