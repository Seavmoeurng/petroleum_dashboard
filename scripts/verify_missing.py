import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    ext_data = json.load(f)

# Let's aggregate all information per country from all sheets!
countries_map = {}

# 1. Sheet 1.Storage
for row in ext_data['excel']['1.Storage'][2:]:
    if len(row) > 1 and row[1]:
        cname = row[1].strip()
        countries_map[cname] = {
            'rank': row[0],
            'tradeStatus': row[2],
            'provenReserves': row[3],
            'regulatoryAuthority': row[4],
            'resourceOwnership': row[5],
            'upstreamModel': row[6],
            'strategicStoragePolicy': row[7],
            'storageSprCapacity': row[8]
        }

# 2. Sheet 2. Policy Benchmark
for row in ext_data['excel']['2. Policy Benchmark'][2:]:
    if len(row) > 0 and row[0]:
        cname = row[0].strip()
        if cname in countries_map:
            countries_map[cname]['primaryPolicyFramework'] = row[1]
            countries_map[cname]['policyYearValidity'] = row[2]
            countries_map[cname]['upstreamPolicyStrategy'] = row[3]
            countries_map[cname]['downstreamPolicyStrategy'] = row[4]
            countries_map[cname]['riskManagementFramework'] = row[5]
            countries_map[cname]['policyTransferability'] = row[6]

# 3. Sheet third (Real Tax Price & State Revenue Capture)
for row in ext_data['excel']['third'][1:]:
    if len(row) > 0 and row[0]:
        cname = row[0].strip()
        if cname in countries_map:
            countries_map[cname]['primaryFiscalInstruments'] = row[1]
            countries_map[cname]['royaltyBaseTax'] = row[2]
            countries_map[cname]['cit'] = row[3]
            countries_map[cname]['costRecoveryIncentives'] = row[4]
            countries_map[cname]['estStateRevenueCapture'] = row[5]
            countries_map[cname]['realTaxPrice'] = row[6]

# 4. Sheet 3. Fiscal Benchmark (Upstream & Downstream Tax Breakdown)
for row in ext_data['excel']['3. Fiscal Benchmark'][3:]:
    if len(row) > 0 and row[0]:
        cname = row[0].strip()
        if cname in countries_map:
            countries_map[cname]['upstreamRoyalty'] = row[1]
            countries_map[cname]['upstreamCIT'] = row[2]
            countries_map[cname]['upstreamPetroleumTax'] = row[3]
            countries_map[cname]['signatureBonus'] = row[4]
            countries_map[cname]['contractModel'] = row[5]
            countries_map[cname]['whoPays'] = row[6]
    if len(row) > 7 and row[7]:
        cname2 = row[7].strip()
        if cname2 in countries_map:
            countries_map[cname2]['downstreamImportDuty'] = row[8]
            countries_map[cname2]['downstreamExcise'] = row[9]
            countries_map[cname2]['downstreamVAT'] = row[10]
            countries_map[cname2]['downstreamCarbonTax'] = row[11]
            countries_map[cname2]['priceRegulation'] = row[12]
            countries_map[cname2]['taxCollectedBy'] = row[13]

# 5. Sheet 4.Reference (Institutions, Documents, Source Links)
for row in ext_data['excel']['4.Reference'][2:]:
    if len(row) > 1 and row[1]:
        cname = row[1].strip()
        if cname in countries_map:
            countries_map[cname]['keyInstitutions'] = row[2]
            countries_map[cname]['keyDocument'] = row[3]
            sources = [row[i] for i in [4, 5, 6] if i < len(row) and row[i] and row[i].startswith('http')]
            countries_map[cname]['sources'] = sources

print(f"Extracted aggregated countries count: {len(countries_map)}")
print("\nSample aggregated data for Saudi Arabia:")
print(json.dumps(countries_map.get("Saudi Arabia", {}), indent=2, ensure_ascii=False))

