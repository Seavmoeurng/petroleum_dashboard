import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    ext_data = json.load(f)

# Let's write a comprehensive builder for petroleum_data.js
# We collect all raw rows and construct clean JS objects for the 11 countries.

countries_info = {
    "venezuela": {"id": "venezuela", "country": "Venezuela", "rank": 1, "tradeStatus": "Net Exporter"},
    "saudi-arabia": {"id": "saudi-arabia", "country": "Saudi Arabia", "rank": 2, "tradeStatus": "Net Exporter"},
    "iran": {"id": "iran", "country": "Iran", "rank": 3, "tradeStatus": "Net Exporter"},
    "canada": {"id": "canada", "country": "Canada", "rank": 4, "tradeStatus": "Both"},
    "iraq": {"id": "iraq", "country": "Iraq", "rank": 5, "tradeStatus": "Net Exporter"},
    "united-arab-emirates": {"id": "united-arab-emirates", "country": "United Arab Emirates", "rank": 6, "tradeStatus": "Net Exporter"},
    "kuwait": {"id": "kuwait", "country": "Kuwait", "rank": 7, "tradeStatus": "Net Exporter"},
    "russia": {"id": "russia", "country": "Russia", "rank": 8, "tradeStatus": "Net Exporter"},
    "united-states": {"id": "united-states", "country": "United States", "rank": 11, "tradeStatus": "Both"},
    "china": {"id": "china", "country": "China", "rank": 13, "tradeStatus": "Both"},
    "brazil": {"id": "brazil", "country": "Brazil", "rank": 15, "tradeStatus": "Both"},
}

print("Configured country list count:", len(countries_info))
