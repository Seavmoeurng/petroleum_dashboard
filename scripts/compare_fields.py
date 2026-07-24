import json
import re

with open('petroleum_data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    ext_data = json.load(f)

print("Checking fields in petroleum_data.js...")
sample_country = "saudi-arabia"
print("Sample JS structure snippet:")

# Let's inspect what fields are in petroleum_data.js for Saudi Arabia
start = js_content.find('id: "saudi-arabia"')
end = js_content.find('id: "united-states"')
print(js_content[start:start+1200])

