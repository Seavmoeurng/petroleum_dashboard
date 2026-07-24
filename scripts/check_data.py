import json
import re

with open('petroleum_data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

country_blocks = js_content.split('id: "')
print(f"Total entries in petroleum_data.js: {len(country_blocks)-1}")

for block in country_blocks[1:]:
    cid = block.split('"')[0]
    cname_match = re.search(r'country:\s*"([^"]+)"', block)
    cname = cname_match.group(1) if cname_match else cid
    rank_match = re.search(r'rank:\s*(\d+)', block)
    rank = rank_match.group(1) if rank_match else 'N/A'
    print(f"ID: {cid} | Name: {cname} | Rank: {rank}")
