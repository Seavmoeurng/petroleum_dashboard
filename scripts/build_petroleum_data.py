import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Detailed compilation of all extracted information from 1.pdf, 2.pdf, 3.pdf, 4.pdf and Excel sheets
complete_dataset = [
  {
    "id": "venezuela",
    "country": "Venezuela",
    "rank": 1,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Ministry of Petroleum",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Majority State JV",
    
    "oilReserveSpr": {
      "provenReserves": "~300-303 Billion bbls (Rank #1)",
      "provenReservesNumeric": 303,
      "sprCapacity": "Constrained capacity due to maintenance gaps",
      "ownershipModel": "State Ownership (Ministry of Petroleum)",
      "licensingModel": "Majority State JV (PDVSA mandated 60% majority)",
      "stockDuration": "Constrained operational storage duration",
      "infrastructureMaintenance": "Severe maintenance gaps; aging storage tanks & export infrastructure.",
      "releaseTriggers": "Domestic refinery outages and severe economic supply bottlenecks."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Organic Hydrocarbons Law",
      "policyYearValidity": "2001 (Amended, Active 2026)",
      "explorationLicensing": "Mandatory PDVSA majority (minimum 60%) in all Empresas Mixtas joint ventures.",
      "roleOfNoc": "PDVSA holds absolute state monopoly over operations; constrained by underinvestment and OFAC sanctions.",
      "resourceConservation": "Production capacity severely constrained; aging infrastructure limits HSE compliance."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Collapsed refining sector operating far below installed capacity; severe domestic supply deficits.",
      "retailPricingSubsidy": "Dual-market retail pricing (heavily subsidized vs. international USD pricing bands).",
      "fuelQualityEnvStandards": "Low environmental compliance due to operational deficits; high flaring rate.",
      "importDuty": "Not Found",
      "exciseTax": "General Sales Tax",
      "vatGst": "16% (Implementation failing due to dual market)",
      "carbonTax": "None",
      "priceRegulation": "Government controlled (Dual pricing)",
      "taxCollectedBy": "SENIAT"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Royalty + Hydrocarbon Tax + State Participation",
      "royalties": "33.33% statutory (can reduce to 20% or lower for mature/heavy oil fields).",
      "pptCit": "50% Hydrocarbon Extraction Tax",
      "petroleumSpecificTax": "Extraction Tax (33.33% net of royalty) + Windfall Taxes",
      "signatureBonus": "Required (Sign-on bonuses for JVs)",
      "contractModel": "Joint Venture (Empresas Mixtas)",
      "whoPays": "Joint venture operators",
      "costRecoveryRules": "Moving towards contract & fiscal flexibility under new emergency energy laws.",
      "estStateRevenueCapture": "Discretionary Royalty + Integrated Tax",
      "realTaxPrice": "Total State Capture: ~$20.75/bbl (~25% of gross @ $83/bbl)",
      "investmentIncentives": "Flexible terms offered to foreign JV partners to attract E&P capital.",
      "comprehensiveTaxSchedule": "Upstream: 33.33% Royalty + 50% CIT | Downstream: 16% Sales Tax / VAT."
    },

    "riskManagement": {
      "hseCompliance": "Aging infrastructure and reduced refining capacity increase operational & environmental risks.",
      "financialRiskRevenueStabilization": "Sovereign default & OFAC sanctions hamper international crude sales.",
      "geopoliticalLocalContent": "High reliance on foreign dilution heavy crude imports; FONDEN social development contributions.",
      "climateEnergyTransition": "Minimal transition focus; immediate priority on basic field rehabilitation."
    },

    "transferabilityToCambodia": "Macroeconomic stability is essential; rigid petroleum policies struggle if underlying state economy is unstable.",
    
    "keyInstitutions": "Ministry of Petroleum, PDVSA",
    "keyDocument": "OPEC Annual Statistical Bulletin (Venezuela Data)",
    "references": [
      "OPEC Annual Statistical Bulletin 2024",
      "EIA Venezuela Country Analysis Brief",
      "Organic Hydrocarbons Law (2001)"
    ],
    "sources": [
      { "name": "OPEC ASB", "url": "https://asb.opec.org/" },
      { "name": "EIA Venezuela Analysis", "url": "https://www.eia.gov/international/analysis/country/VEN" },
      { "name": "ICLG Hydrocarbons Law", "url": "https://iclg.com/practice-areas/oil-and-gas-laws-and-regulations/venezuela/" }
    ]
  },

  {
    "id": "saudi-arabia",
    "country": "Saudi Arabia",
    "rank": 2,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Ministry of Energy",
    "resourceOwnership": "100% State Ownership",
    "upstreamModel": "State Monopoly",

    "oilReserveSpr": {
      "provenReserves": "~267 Billion bbls (Rank #2)",
      "provenReservesNumeric": 267,
      "sprCapacity": "~82 Million bbls operational on-land",
      "ownershipModel": "100% State Ownership (Ministry of Energy)",
      "licensingModel": "State Monopoly (Saudi Aramco)",
      "stockDuration": "Strategic operational buffer (>60 days domestic demand)",
      "infrastructureMaintenance": "Extensive domestic on-land tank farm network & pipeline float continuously maintained by Aramco.",
      "releaseTriggers": "OPEC+ market stabilization directives, severe domestic refinery outages, or regional export chokepoint disruptions."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Hydrocarbon Law & Saudi Vision 2030",
      "policyYearValidity": "2017 & 2016 (Current to 2026)",
      "explorationLicensing": "Restricted state concession granted exclusively to Saudi Aramco under Hydrocarbon Law.",
      "roleOfNoc": "Monopolistic state entity (Saudi Aramco) manages 100% of crude exploration, drilling, production, and field development.",
      "resourceConservation": "Strict Maximum Sustainable Capacity (MSC) caps at ~12M bpd; aggressive water-injection & reservoir pressure maintenance."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Massive domestic refining capacity + East-West Pipeline (5M bpd) bypassing the Strait of Hormuz to Yanbu on the Red Sea.",
      "retailPricingSubsidy": "Domestic fuel retail prices regulated and linked to global price bands under fiscal reform policies.",
      "fuelQualityEnvStandards": "Transitioning domestic transport fuel to Euro V / Saudi SASO ultra-low sulfur specifications.",
      "importDuty": "Varies (Exemptions apply)",
      "exciseTax": "None",
      "vatGst": "15%",
      "carbonTax": "None",
      "priceRegulation": "Government controlled",
      "taxCollectedBy": "ZATCA / Ministry of Energy"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Variable Royalty + 50% CIT + State Ownership",
      "royalties": "15% to 45% Brent-linked progressive sliding-scale royalty on gross production.",
      "pptCit": "50% Corporate Income Tax (CIT) on hydrocarbon extraction activities.",
      "petroleumSpecificTax": "None",
      "signatureBonus": "None",
      "contractModel": "Concession",
      "whoPays": "Hydrocarbon producers (Saudi Aramco)",
      "costRecoveryRules": "Extremely low lifting costs maximize state rent; Aramco absorbs operational CapEx directly.",
      "estStateRevenueCapture": "Royalty + 50% CIT + Aramco Dividends",
      "realTaxPrice": "Upstream: ~$47.67/bbl (~57% of gross @ $83/bbl)",
      "investmentIncentives": "Aramco retains CapEx allocation for MSC maintenance & petrochemical integration.",
      "comprehensiveTaxSchedule": "Upstream: 15-45% Royalty + 50% CIT | Downstream: 15% VAT collected by ZATCA."
    },

    "riskManagement": {
      "hseCompliance": "Strict internal Aramco environmental & safety standards; zero routine flaring target by 2030.",
      "financialRiskRevenueStabilization": "OPEC+ production quota leadership stabilizes global Brent crude price; Public Investment Fund (PIF) diversifies national wealth.",
      "geopoliticalLocalContent": "East-West Pipeline mitigates Strait of Hormuz blockade risk; iktva program mandates >70% local content procurement.",
      "climateEnergyTransition": "Major investments in CCUS (Carbon Capture), green hydrogen, and solar power integration at extraction fields."
    },

    "transferabilityToCambodia": "Strategic infrastructure investment (bypass pipelines) and establishing a strong state NOC governance structure.",

    "keyInstitutions": "Ministry of Energy, Saudi Aramco",
    "keyDocument": "Saudi Aramco Annual Report 2024",
    "references": [
      "Saudi Aramco Annual Report 2024",
      "Law of Petroleum and Petrochemical Products (Royal Decree M/37)",
      "Saudi Vision 2030 Energy Framework"
    ],
    "sources": [
      { "name": "Saudi Aramco Portal", "url": "https://www.saudiaramco.com/" },
      { "name": "OPEC Member Profile", "url": "https://www.opec.org/opec_web/en/about_us/169.htm" },
      { "name": "MISA Petroleum Law", "url": "https://misa.gov.sa/app/uploads/2025/07/Law-of-Petroleum-and-Petrochemical-Products.pdf" }
    ]
  },

  {
    "id": "iran",
    "country": "Iran",
    "rank": 3,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Ministry of Petroleum",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Risk Service Contract (IPC)",

    "oilReserveSpr": {
      "provenReserves": "~208 Billion bbls (Rank #3)",
      "provenReservesNumeric": 208,
      "sprCapacity": "~71 Million bbls floating storage",
      "ownershipModel": "State Ownership (Ministry of Petroleum / NIOC)",
      "licensingModel": "Risk Service Contract (Iran Petroleum Contract - IPC)",
      "stockDuration": "Floating operational buffer on offshore VLCC tankers",
      "infrastructureMaintenance": "NITC (National Iranian Tanker Co.) floating storage fleet and Kharg Island export terminal.",
      "releaseTriggers": "Sanctions avoidance logistics and international market export windows."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Petroleum Act & IPC Framework",
      "policyYearValidity": "1987 & 2016 (Active Framework 2026)",
      "explorationLicensing": "NIOC absolute monopoly; foreign entry restricted to IPC risk-service contracts with no resource equity.",
      "roleOfNoc": "NIOC (National Iranian Oil Co.) retains 100% resource ownership & field operation rights.",
      "resourceConservation": "Production constrained by sanctions and lack of modern gas-reinjection EOR technology."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Large domestic refining capacity focusing on domestic gasoline self-sufficiency.",
      "retailPricingSubsidy": "Extensive domestic retail subsidies leading to high cross-border fuel smuggling rates.",
      "fuelQualityEnvStandards": "Euro IV / V transition slow due to equipment import restrictions under trade sanctions.",
      "importDuty": "4% Base",
      "exciseTax": "Varies (Absorbed in regulated retail price)",
      "vatGst": "9%",
      "carbonTax": "Green Tax (1% on polluting industrial facilities)",
      "priceRegulation": "Government controlled (Dual quota pricing system)",
      "taxCollectedBy": "Iranian National Tax Administration (INTA)"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Iran Petroleum Contract (IPC) - Risk Service Contract",
      "royalties": "None (No traditional concession royalty under constitution)",
      "pptCit": "25% CIT for foreign entities under IPC framework",
      "petroleumSpecificTax": "None (Service fee model)",
      "signatureBonus": "None",
      "contractModel": "Risk Service Contract (IPC)",
      "whoPays": "Foreign IPC contractors",
      "costRecoveryRules": "Approved OPEX & CAPEX recovery plus a fixed fee per barrel.",
      "estStateRevenueCapture": "IPC Cost Recovery + State Remuneration Fee",
      "realTaxPrice": "State Capture: ~$58-$60/bbl (>90% rent @ $83/bbl)",
      "investmentIncentives": "Higher remuneration fees offered for technically challenging offshore & EOR fields.",
      "comprehensiveTaxSchedule": "Upstream: IPC Service Fee + 25% CIT | Downstream: 9% VAT + 1% Green Tax."
    },

    "riskManagement": {
      "hseCompliance": "Aging offshore platforms & refineries limit HSE compliance.",
      "financialRiskRevenueStabilization": "Subsidies strain national budget; high exposure to sanctions & international financial restrictions.",
      "geopoliticalLocalContent": "Goreh-Jask pipeline constructed to bypass Strait of Hormuz to the Gulf of Oman.",
      "climateEnergyTransition": "High gas flaring rates; renewable energy initiatives under-resourced."
    },

    "transferabilityToCambodia": "Fuel subsidy reforms should balance social affordability with fiscal sustainability.",

    "keyInstitutions": "Ministry of Petroleum, NIOC",
    "keyDocument": "OPEC Annual Statistical Bulletin (Iran Data)",
    "references": [
      "OPEC Annual Statistical Bulletin 2024",
      "Petroleum Act of 1987 (As Amended 2016)",
      "EIA Iran Country Analysis"
    ],
    "sources": [
      { "name": "OPEC Iran Bulletin", "url": "https://asb.opec.org/" },
      { "name": "EIA Iran Analysis", "url": "https://www.eia.gov/international/analysis/country/IRN" },
      { "name": "IEA Iran Policy Database", "url": "https://www.iea.org/policies/12289-petroleum-act-of-1987-as-amended" }
    ]
  },

  {
    "id": "canada",
    "country": "Canada",
    "rank": 4,
    "tradeStatus": "Both",
    "regulatoryAuthority": "Federal: CER / Provincial: AER",
    "resourceOwnership": "Provincial Crown Ownership",
    "upstreamModel": "Open Concession",

    "oilReserveSpr": {
      "provenReserves": "~163 Billion bbls (Rank #4)",
      "provenReservesNumeric": 163,
      "sprCapacity": "Commercial Hub Storage (>90 Days demand)",
      "ownershipModel": "Provincial Crown mineral ownership with private operating rights",
      "licensingModel": "Open Concession (Provincial Crown Auctions)",
      "stockDuration": ">90 days demand satisfied via commercial private storage hubs in Alberta & Saskatchewan.",
      "infrastructureMaintenance": "Private commercial tank farms & pipeline storage hubs (Hardisty, Edmonton) maintained by Enbridge and TC Energy.",
      "releaseTriggers": "Commercial market arbitrage & IEA coordinated stockdraw obligations."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Provincial Royalty Frameworks & CER Act",
      "policyYearValidity": "2019 (Active Framework 2026)",
      "explorationLicensing": "Provincial Crown land tenure auctions governed by AER (Alberta) and Ministry of Energy.",
      "roleOfNoc": "No National Oil Company (NOC); private commercial oil sands and conventional producers.",
      "resourceConservation": "Strict oil sands tailings management, SAGD reservoir optimization, and provincial carbon emissions limits."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Trans Mountain Expansion (TMX) pipeline (890k bpd) opens Pacific export routes; extensive crude-by-rail backup.",
      "retailPricingSubsidy": "Free-market pricing governed by transparent market competition; carbon tax transparently added to pump price.",
      "fuelQualityEnvStandards": "Federal Clean Fuel Regulations (CFR) requiring carbon intensity reductions across fuel suppliers.",
      "importDuty": "0% (CUSMA); Varies for non-free trade partners",
      "exciseTax": "Federal: $0.10/L gas, $0.04/L diesel + Provincial fuel taxes",
      "vatGst": "5% GST + Provincial PST/HST (Total ~13-15%)",
      "carbonTax": "Federal Carbon Tax (~0.17 CAD/L)",
      "priceRegulation": "Mixed (Mostly liberalized; regulated in Atlantic provinces)",
      "taxCollectedBy": "Canada Revenue Agency (CRA) / Provincial Governments"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Sliding-scale Royalty + CIT",
      "royalties": "Sliding-scale royalty based on project payout (Alberta: 1%-9% pre-payout, 25%-40% post-payout based on WTI price).",
      "pptCit": "Combined Federal (15%) + Provincial (8%-12%) CIT total ~23-27%.",
      "petroleumSpecificTax": "None (Crown royalties act as main rent capture)",
      "signatureBonus": "Required (Lease auction bonus bids)",
      "contractModel": "Concession",
      "whoPays": "Private oil companies",
      "costRecoveryRules": "Low pre-payout royalties accelerate CapEx write-off before higher post-payout rates apply.",
      "estStateRevenueCapture": "Sliding-scale Royalty + CIT + Carbon Tax",
      "realTaxPrice": "Upstream Pre-payout: ~$6.12/bbl; Scales to ~40% net post-payout",
      "investmentIncentives": "CapEx write-offs & clean technology investment tax credits (CCUS).",
      "comprehensiveTaxSchedule": "Upstream: 1-40% Royalty + ~23% CIT | Downstream: Federal Excise ($0.10/L) + Carbon Tax + GST."
    },

    "riskManagement": {
      "hseCompliance": "Strict AER environmental oversight & oil sands monitoring programs.",
      "financialRiskRevenueStabilization": "Alberta Heritage Savings Trust Fund manages fiscal price volatility.",
      "geopoliticalLocalContent": "TMX pipeline diversifies crude exports away from exclusive US Gulf Coast market reliance.",
      "climateEnergyTransition": "Federal 2030 Emissions Reduction Plan and oil sands Pathways Alliance net-zero initiative."
    },

    "transferabilityToCambodia": "A petroleum stabilization fund (like Alberta Heritage Fund) could help reduce national fiscal volatility.",

    "keyInstitutions": "Federal: CER / Provincial: AER",
    "keyDocument": "CER Annual Report of the Commission 2023-24",
    "references": [
      "CER Annual Report 2023-24",
      "Alberta Energy Regulator (AER) Guidelines",
      "Canadian Environmental Protection Act"
    ],
    "sources": [
      { "name": "CER Canada Portal", "url": "https://www.cer-rec.gc.ca/" },
      { "name": "EIA Canada Brief", "url": "https://www.eia.gov/international/analysis/country/CAN" },
      { "name": "CAPP Energy Association", "url": "https://www.capp.ca" }
    ]
  },

  {
    "id": "iraq",
    "country": "Iraq",
    "rank": 5,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Federal: Ministry of Oil / Regional: KRG MNR",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Technical Service Contract (TSC)",

    "oilReserveSpr": {
      "provenReserves": "~145 Billion bbls (Rank #5)",
      "provenReservesNumeric": 145,
      "sprCapacity": "Minimal operational export terminal buffer",
      "ownershipModel": "State Ownership (Federal Ministry of Oil / KRG MNR)",
      "licensingModel": "Technical Service Contract (TSC) / KRG PSA",
      "stockDuration": "Minimal operational buffer (<15 days)",
      "infrastructureMaintenance": "Basra Oil Terminal, Fao tank farm & Ceyhan pipeline network requiring major rehabilitation.",
      "releaseTriggers": "Southern port export weather delays and pipeline flow disruptions."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Federal Refining Law & Draft Oil/Gas Law",
      "policyYearValidity": "2007 Draft (Operating Basis 2026)",
      "explorationLicensing": "Federal TSCs via licensing rounds; KRG utilizes Production Sharing Agreements (PSAs).",
      "roleOfNoc": "State Oil Companies (Basra Oil Co., North Oil Co., SOMO) maintain 100% resource title & mandatory 25% state partner equity.",
      "resourceConservation": "Major common seawater supply project (CSSP) needed for reservoir pressure maintenance in giant southern fields."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Karbala & Baiji refineries expanded to reduce fuel import reliance; Ceyhan export pipeline currently stalled.",
      "retailPricingSubsidy": "Heavy state retail fuel subsidies; inland storage prioritized for domestic power generation.",
      "fuelQualityEnvStandards": "Upgrading domestic refining slate to reduce heavy fuel oil surplus and meet Euro V standards.",
      "importDuty": "Exemptions apply for state oil company imports",
      "exciseTax": "Not Found",
      "vatGst": "None (Subject to general sales tax)",
      "carbonTax": "None",
      "priceRegulation": "Government controlled",
      "taxCollectedBy": "General Commission for Taxes / KRG Ministry of Finance"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Technical Service Contract (Fixed Remuneration Fee)",
      "royalties": "None federally (10% under KRG PSAs)",
      "pptCit": "35% CIT on foreign contractor remuneration fees",
      "petroleumSpecificTax": "Fixed Remuneration Fee ($1.50-$5.50/bbl)",
      "signatureBonus": "Required (Sign-on bonuses in licensing rounds)",
      "contractModel": "Technical Service Contract (TSC)",
      "whoPays": "International oil contractors",
      "costRecoveryRules": "IOCs recover 100% of approved OPEX & CAPEX plus fixed fee per barrel.",
      "estStateRevenueCapture": "Fixed Fee TSC (State retains >95% crude value)",
      "realTaxPrice": "State Capture: ~$76.50/bbl (>95% rent @ $83/bbl)",
      "investmentIncentives": "Remuneration fee indexation and rapid cost recovery provisions.",
      "comprehensiveTaxSchedule": "Upstream: Fixed TSC Fee + 35% CIT | Downstream: Subsidized pump pricing."
    },

    "riskManagement": {
      "hseCompliance": "High security protection investments required; flaring reduction programs underway with TotalEnergies.",
      "financialRiskRevenueStabilization": "Federal government budget heavily exposed to crude price swings; oil revenues fund state payroll.",
      "geopoliticalLocalContent": "Vulnerability due to Federal vs KRG regulatory disputes and Strait of Hormuz transit dependence.",
      "climateEnergyTransition": "Gas growth project aimed at capturing 600 MSCFD flared gas for power generation."
    },

    "transferabilityToCambodia": "Technical Service Contracts (TSCs) can be evaluated to maintain sovereign state resource ownership while hiring foreign expertise.",

    "keyInstitutions": "Ministry of Oil, SOMO, KRG MNR",
    "keyDocument": "Iraq EITI Report (Extractive Industries Transparency Initiative)",
    "references": [
      "Iraq EITI Report 2024",
      "Draft Federal Oil and Gas Law of Iraq",
      "EIA Iraq Country Analysis Brief"
    ],
    "sources": [
      { "name": "EITI Iraq Portal", "url": "https://eiti.org/countries/iraq" },
      { "name": "EIA Iraq Analysis", "url": "https://www.eia.gov/international/analysis/country/IRQ" },
      { "name": "World Bank Iraq Overview", "url": "https://www.worldbank.org/en/country/iraq/overview" }
    ]
  },

  {
    "id": "united-arab-emirates",
    "country": "United Arab Emirates",
    "rank": 6,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Ministry of Energy and Infrastructure / SPC",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Majority State JV",

    "oilReserveSpr": {
      "provenReserves": "~113 Billion bbls (Rank #6)",
      "provenReservesNumeric": 113,
      "sprCapacity": "~34 Million bbls on-land storage",
      "ownershipModel": "State Ownership (Abu Dhabi Supreme Council for Financial and Economic Affairs)",
      "licensingModel": "Majority State JV (ADNOC mandates 60% majority equity)",
      "stockDuration": "Strategic commercial & operational buffer at Port of Fujairah",
      "infrastructureMaintenance": "Fujairah deepwater terminal & tank farm hub with continuous expansion.",
      "releaseTriggers": "Commercial market arbitrage & Gulf export security emergencies."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "UAE Energy Strategy 2050 & Concession Rules",
      "policyYearValidity": "2017 (Updated 2023, Active 2026)",
      "explorationLicensing": "Competitive concession bidding rounds; ADNOC is mandatory majority partner (60%) in all concessions.",
      "roleOfNoc": "ADNOC (Abu Dhabi National Oil Co.) manages production targets & maximum sustainable capacity increases to 5M bpd by 2027.",
      "resourceConservation": "Industry-leading zero routine flaring target and extensive CCUS implementation in offshore fields."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Ruwais mega-refining complex + ADCOP pipeline (1.5M bpd) pumping crude directly to Fujairah outside the Strait of Hormuz.",
      "retailPricingSubsidy": "Fully liberalized retail pricing tied to international monthly benchmarks since 2015.",
      "fuelQualityEnvStandards": "Strict Euro V transport fuel standards; green hydrogen & SAF aviation fuel investments.",
      "importDuty": "5% GCC unified tariff",
      "exciseTax": "None on transport fuel",
      "vatGst": "5%",
      "carbonTax": "None",
      "priceRegulation": "Formula-based (Adjusted monthly by Ministry committee)",
      "taxCollectedBy": "Federal Tax Authority (FTA)"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Royalty + Concession CIT + ADNOC State Equity",
      "royalties": "Base royalty on gross production (~20% concession-specific).",
      "pptCit": "55% to 85% Upstream Corporate Income Tax on foreign concession partners.",
      "petroleumSpecificTax": "None",
      "signatureBonus": "Required (Concession sign-on bonuses)",
      "contractModel": "Concession / Majority State JV",
      "whoPays": "Foreign concession holders",
      "costRecoveryRules": "Proportionate OPEX & CAPEX recovery before tax calculation.",
      "estStateRevenueCapture": "Royalty + 55-85% CIT + ADNOC Dividends",
      "realTaxPrice": "Upstream: ~$55.60/bbl (~67% of gross @ $83/bbl)",
      "investmentIncentives": "In-Country Value (ICV) certification grants preferred status in CapEx procurement.",
      "comprehensiveTaxSchedule": "Upstream: ~20% Royalty + 55-85% CIT | Downstream: 5% VAT collected by FTA."
    },

    "riskManagement": {
      "hseCompliance": "ADNOC stringent HSE policy framework; zero-flaring & decarbonization targets.",
      "financialRiskRevenueStabilization": "Abu Dhabi Investment Authority (ADIA) sovereign fund absorbs oil price cycles.",
      "geopoliticalLocalContent": "ADCOP pipeline bypasses Strait of Hormuz to Fujairah; ICV program mandates local procurement.",
      "climateEnergyTransition": "UAE Energy Strategy 2050 targets net-zero by 2050 with $54B renewable energy commitment."
    },

    "transferabilityToCambodia": "Mandating NOC participation (e.g. 60% state equity) in joint ventures ensures technology transfer and strong state oversight.",

    "keyInstitutions": "Ministry of Energy & Infrastructure, ADNOC",
    "keyDocument": "UAE Energy Strategy 2050",
    "references": [
      "UAE Energy Strategy 2050 (Updated 2023)",
      "ADNOC In-Country Value (ICV) Program Guidelines",
      "EIA UAE Country Analysis"
    ],
    "sources": [
      { "name": "Ministry of Energy Portal", "url": "https://www.moei.gov.ae/en/about-ministry/uae-energy-strategy-2050.aspx" },
      { "name": "EIA UAE Brief", "url": "https://www.eia.gov/international/analysis/country/ARE" },
      { "name": "IEA UAE Profile", "url": "https://www.iea.org/countries/united-arab-emirates" }
    ]
  },

  {
    "id": "kuwait",
    "country": "Kuwait",
    "rank": 7,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Ministry of Oil",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Technical Service Agreement (TSA)",

    "oilReserveSpr": {
      "provenReserves": "~101 Billion bbls (Rank #7)",
      "provenReservesNumeric": 101,
      "sprCapacity": "Export terminal buffer",
      "ownershipModel": "State Ownership (Ministry of Oil / KPC)",
      "licensingModel": "Technical Service Agreement (TSA)",
      "stockDuration": "Operational storage buffer at Mina Al-Ahmadi & Mina Abdulla terminals",
      "infrastructureMaintenance": "KOC tank farm clusters & offshore crude loading facilities.",
      "releaseTriggers": "Export loading delays and Arabian Gulf maritime security emergencies."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Law No. 6 of 1980 (KPC) & 2040 Strategy",
      "policyYearValidity": "1980 & 2021 (Active Framework 2026)",
      "explorationLicensing": "Absolute state monopoly; constitutional prohibition of foreign resource ownership or concessions.",
      "roleOfNoc": "KPC (Kuwait Petroleum Corp) & KOC (Kuwait Oil Co.) manage 100% of crude exploration & production.",
      "resourceConservation": "Managing pressure depletion in the massive Burgan field via advanced water injection."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Al-Zour mega-refinery (615k bpd) producing clean low-sulfur fuel oil for domestic power & export.",
      "retailPricingSubsidy": "Heavily subsidized domestic fuel and electricity pricing.",
      "fuelQualityEnvStandards": "Clean Fuels Project completed; domestic & export refining upgraded to Euro V ultra-low sulfur standards.",
      "importDuty": "Varies (Domestic petroleum exempt)",
      "exciseTax": "None",
      "vatGst": "None (Not yet implemented)",
      "carbonTax": "None",
      "priceRegulation": "Government controlled",
      "taxCollectedBy": "Ministry of Finance"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Technical Service Agreement (TSA) - Fixed Service Fees",
      "royalties": "None (100% state resource ownership)",
      "pptCit": "15% CIT (Applies only to foreign contractor service fees; KPC/KOC exempt)",
      "petroleumSpecificTax": "None",
      "signatureBonus": "None",
      "contractModel": "Technical Service Agreement (TSA)",
      "whoPays": "Foreign service contractors",
      "costRecoveryRules": "Contractors paid fixed service fees & incentive bonuses; no crude ownership.",
      "estStateRevenueCapture": "TSA Service Fee (State captures ~100% net rent)",
      "realTaxPrice": "State Capture: ~$78-$80/bbl (100% rent @ $83/bbl)",
      "investmentIncentives": "Performance-based incentive bonuses for enhanced heavy oil recovery.",
      "comprehensiveTaxSchedule": "Upstream: 100% State Net Rent | Downstream: Subsidized retail prices."
    },

    "riskManagement": {
      "hseCompliance": "KOC rigorous HSE management system; lowering gas flaring below 1%.",
      "financialRiskRevenueStabilization": "Kuwait Investment Authority (KIA) Sovereign Wealth Fund mitigates long-term oil price shocks.",
      "geopoliticalLocalContent": "High strategic reliance on the Strait of Hormuz for export logistics.",
      "climateEnergyTransition": "KPC 2050 Decarbonization Strategy targeting net-zero Scope 1 & 2 emissions."
    },

    "transferabilityToCambodia": "Technical Service Agreements (TSAs) can facilitate technology acquisition without ceding national equity.",

    "keyInstitutions": "Ministry of Oil, KPC, KOC",
    "keyDocument": "KPC Strategy 2040",
    "references": [
      "KPC 2040 Strategic Directions",
      "Law No. 6 of 1980 Establishing KPC",
      "EIA Kuwait Country Analysis"
    ],
    "sources": [
      { "name": "KPC Corporate Portal", "url": "https://www.kpc.com.kw/our-business/strategy-2040" },
      { "name": "EIA Kuwait Analysis", "url": "https://www.eia.gov/international/analysis/country/KWT" },
      { "name": "OPEC Kuwait Statistics", "url": "https://publications.opec.org/asb" }
    ]
  },

  {
    "id": "russia",
    "country": "Russia",
    "rank": 8,
    "tradeStatus": "Net Exporter",
    "regulatoryAuthority": "Minenergo / Rosnedra",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Majority State JV",

    "oilReserveSpr": {
      "provenReserves": "~80 Billion bbls (Rank #8)",
      "provenReservesNumeric": 80,
      "sprCapacity": "Continuous Transneft pipeline float & commercial storage",
      "ownershipModel": "State Subsoil Ownership (Minenergo / Rosnedra)",
      "licensingModel": "Subsoil Licensing / Majority State JV (Rosneft, Gazprom Neft)",
      "stockDuration": "Continuous logistical float across Transneft trunk pipeline grid",
      "infrastructureMaintenance": "Transneft pipeline network (over 50,000 km) and Baltic / Pacific port terminals (Primorsk, Kozmino).",
      "releaseTriggers": "Export reorientation logistics & refinery maintenance scheduling."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Law on Subsoil & Energy Strategy 2035",
      "policyYearValidity": "1992 & 2020 (Active Framework 2026)",
      "explorationLicensing": "Subsoil auctions managed by Rosnedra; strategic offshore & Arctic fields restricted to state NOCs.",
      "roleOfNoc": "State-backed NOCs (Rosneft, Gazprom Neft) dominate crude extraction.",
      "resourceConservation": "Optimizing extraction from mature Western Siberian fields via horizontal drilling and hydrofracking."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Complete reorientation of crude export logistics from Europe toward China & India via ESPO pipeline and dark fleet tankers.",
      "retailPricingSubsidy": "Government intervention via the Damper Mechanism to subsidize domestic refineries & cap pump prices.",
      "fuelQualityEnvStandards": "GOST / Technical Regulations (Euro 5 equivalent domestic standards).",
      "importDuty": "Varies by customs union",
      "exciseTax": "Specific excise taxes (~15,000+ RUB/tonne indexed annually)",
      "vatGst": "20%",
      "carbonTax": "Ecological Fee",
      "priceRegulation": "Government controlled (via Damper mechanism)",
      "taxCollectedBy": "Federal Tax Service / MinFin"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "NDPI + NDD + Export Duties",
      "royalties": "None (Replaced by NDPI - Mineral Extraction Tax tied to Urals price formula).",
      "pptCit": "25% CIT (Effective 2025 tax code amendment).",
      "petroleumSpecificTax": "NDPI (Extraction Tax) + NDD (Additional Income Tax - 50% on profit for select fields)",
      "signatureBonus": "Required (Auction bonus payments)",
      "contractModel": "Concession / Subsoil Licensing",
      "whoPays": "Subsoil license holders",
      "costRecoveryRules": "Limited cost recovery under NDPI; NDD provides profit-based tax relief for greenfield projects.",
      "estStateRevenueCapture": "NDPI + NDD + Export Taxes",
      "realTaxPrice": "Net State Take: ~$30.07/bbl (After Damper mechanism @ $83/bbl)",
      "investmentIncentives": "NDD profit-based tax regime applied to Eastern Siberia and Arctic greenfield developments.",
      "comprehensiveTaxSchedule": "Upstream: NDPI + NDD + 25% CIT | Downstream: 20% VAT + Damper mechanism."
    },

    "riskManagement": {
      "hseCompliance": "Rostekhnadzor industrial safety & environmental oversight.",
      "financialRiskRevenueStabilization": "Damper mechanism stabilizes domestic retail fuel prices regardless of global Brent/Urals swings.",
      "geopoliticalLocalContent": "Western sanctions mitigation via alternative maritime logistics and shadow tanker fleets.",
      "climateEnergyTransition": "Energy Strategy 2035 prioritizes maintaining global crude market share."
    },

    "transferabilityToCambodia": "Ensuring tax & fiscal policies secure immediate state revenues from resource extraction while protecting domestic retail consumers.",

    "keyInstitutions": "Minenergo, Rosnedra, MinFin, Transneft",
    "keyDocument": "Energy Strategy of the Russian Federation to 2035",
    "references": [
      "Energy Strategy of Russia to 2035",
      "Law of the Russian Federation on Subsoil (1992)",
      "Tax Code of the Russian Federation (NDPI/NDD Amendments)"
    ],
    "sources": [
      { "name": "Russian Govt Docs", "url": "http://government.ru/docs/39847/" },
      { "name": "EIA Russia Analysis", "url": "https://www.eia.gov/international/analysis/country/RUS" },
      { "name": "IEA Russia Profile", "url": "https://www.iea.org/countries/russia" }
    ]
  },

  {
    "id": "united-states",
    "country": "United States",
    "rank": 11,
    "tradeStatus": "Both",
    "regulatoryAuthority": "Federal: BOEM, BSEE / State Regulators",
    "resourceOwnership": "Mixed Federal, State, and Private",
    "upstreamModel": "Open Concession",

    "oilReserveSpr": {
      "provenReserves": "~47 Billion bbls (Rank #11)",
      "provenReservesNumeric": 47,
      "sprCapacity": "~411-415 Million bbls (Capacity ~714M bbls)",
      "ownershipModel": "Mixed Federal, State, and Private mineral rights ownership",
      "licensingModel": "Open Concession (Competitive Lease Sales)",
      "stockDuration": "~90+ days import protection buffer managed by Department of Energy (DOE)",
      "infrastructureMaintenance": "State-owned salt cavern storage sites (Bryan Mound, Big Hill, West Hackberry, Bayou Choctaw) subject to continuous DOE integrity maintenance.",
      "releaseTriggers": "Presidential emergency declaration during major supply interruptions, severe hurricane damage, or high inflation macroeconomic mitigation."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Energy Policy Act & Inflation Reduction Act",
      "policyYearValidity": "2005 & 2022 (Active Framework 2026)",
      "explorationLicensing": "Decentralized leasing via BOEM (offshore) and BLM (onshore); private landowners lease mineral rights directly to operators.",
      "roleOfNoc": "No National Oil Company (NOC); 100% private IOC and independent commercial oil & gas operators.",
      "resourceConservation": "State regulatory commissions (e.g. Texas Railroad Commission) enforce well spacing, anti-flaring rules, and allowable production rates."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Largest refining capacity globally (Gulf Coast hubs) linked via Colonial & Enbridge pipeline networks.",
      "retailPricingSubsidy": "100% free-market liberalized retail pricing determined by market competition without state subsidies.",
      "fuelQualityEnvStandards": "Strict EPA Clean Air Act Tier 3 gasoline sulfur limits & Renewable Fuel Standard (RFS) ethanol blending mandates.",
      "importDuty": "Varies (~10.5 to 52.5 cents/bbl crude import duty)",
      "exciseTax": "Federal: 18.4 ¢/gal gas, 24.4 ¢/gal diesel + State excise (~32 ¢/gal avg)",
      "vatGst": "None (State & local retail sales taxes vary)",
      "carbonTax": "EPA Oil Spill Liability Trust Fund fee (~9 cents/bbl)",
      "priceRegulation": "Liberalized (Market-based)",
      "taxCollectedBy": "IRS / ONRR / State Revenue Agencies"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Royalty + Federal CIT + State Taxes",
      "royalties": "Federal Onshore: 16.67%; Federal Offshore: 12.5% to 18.75%; Private/State royalties vary (12.5%-25%).",
      "pptCit": "Federal CIT: 21% + State Corporate Income Tax (0%-12%).",
      "petroleumSpecificTax": "State Severance Taxes (e.g., 4.6% crude severance tax in Texas)",
      "signatureBonus": "Required (Competitive lease auction bonus bids)",
      "contractModel": "Concession",
      "whoPays": "Lease holders / Private operators",
      "costRecoveryRules": "Intangible Drilling Costs (IDC) full immediate tax write-offs & percentage depletion allowances.",
      "estStateRevenueCapture": "Royalty + CIT + Severance Tax",
      "realTaxPrice": "Upstream: ~$24.47/bbl (~30% of gross @ $83/bbl)",
      "investmentIncentives": "Inflation Reduction Act (IRA) tax credits for carbon capture (45Q) and clean hydrogen production.",
      "comprehensiveTaxSchedule": "Upstream: Royalty + 21% CIT + Severance Tax | Downstream: Federal Excise (18.4¢/gal gas, 24.4¢/gal diesel) + State Sales Tax."
    },

    "riskManagement": {
      "hseCompliance": "Strict BSEE offshore safety management (SEMS) & EPA environmental protection enforcement.",
      "financialRiskRevenueStabilization": "Free-market futures hedging on NYMEX/ICE; SPR releases act as macroeconomic price buffer.",
      "geopoliticalLocalContent": "Export restriction flexibility; Jones Act shipping requirements for domestic coastal petroleum transport.",
      "climateEnergyTransition": "IRA decarbonization incentives, methane emissions fee, and CCUS tax credits."
    },

    "transferabilityToCambodia": "Maintaining a flexible, private-driven upstream sector while utilizing strategic reserves as a macroeconomic buffer.",

    "keyInstitutions": "DOE, BOEM, BSEE, EPA, FERC",
    "keyDocument": "DOE FY 2024 Annual Performance Report",
    "references": [
      "DOE FY 2024 Annual Performance Report",
      "US Energy Policy Act & Inflation Reduction Act (IRA)",
      "BOEM/BSEE Outer Continental Shelf Lands Act Regulations"
    ],
    "sources": [
      { "name": "Congress IRA Bill", "url": "https://www.congress.gov/bill/109th-congress/house-bill/6" },
      { "name": "EIA US Analysis", "url": "https://www.eia.gov/international/analysis/country/USA" },
      { "name": "IEA US Country Profile", "url": "https://www.iea.org/countries/united-states" }
    ]
  },

  {
    "id": "china",
    "country": "China",
    "rank": 13,
    "tradeStatus": "Both",
    "regulatoryAuthority": "NEA, NDRC, Ministry of Natural Resources",
    "resourceOwnership": "State Ownership",
    "upstreamModel": "Production Sharing Contract (PSC)",

    "oilReserveSpr": {
      "provenReserves": "~26 Billion bbls (Rank #13)",
      "provenReservesNumeric": 26,
      "sprCapacity": "~1.3 - 1.4 Billion bbls combined SPR & commercial quota",
      "ownershipModel": "State Ownership (Ministry of Natural Resources)",
      "licensingModel": "Production Sharing Contract (PSC) / State NOC Monopoly",
      "stockDuration": "~90-100 days import protection buffer across national SPR bases",
      "infrastructureMaintenance": "State-owned strategic reserve bases (Zhoushan, Zhenhai, Dalian, Qingdao) & CNPC/Sinopec commercial tank farms.",
      "releaseTriggers": "NDRC macroeconomic price ceiling enforcement & international supply disruption mitigation."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Mineral Resources Law & 14th Five-Year Plan",
      "policyYearValidity": "1986 (Amended) & 2021 (Active)",
      "explorationLicensing": "NOCs (CNPC, Sinopec, CNOOC) dominate acreage; foreign entry allowed primarily through PSC joint ventures.",
      "roleOfNoc": "State NOCs control >90% of domestic exploration & production.",
      "resourceConservation": "High priority on Enhanced Oil Recovery (EOR), polymer flooding (Daqing field), and deepwater South China Sea exploration."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "World-class refining capacity (Teapot refiners + Sinopec mega-hubs) + Russia ESPO & Central Asia import pipelines.",
      "retailPricingSubsidy": "NDRC adjusts domestic refined fuel prices every 10 working days based on global crude price bands (floor $40, ceiling $130).",
      "fuelQualityEnvStandards": "National VI (Euro 6 equivalent) gasoline & diesel emissions standards nationwide.",
      "importDuty": "1% to 5%",
      "exciseTax": "Consumption Tax (~1.52 RMB/L gas, ~1.20 RMB/L diesel)",
      "vatGst": "13%",
      "carbonTax": "Environmental Protection Tax",
      "priceRegulation": "Government controlled (NDRC formula-based ceiling)",
      "taxCollectedBy": "State Taxation Administration (SAT)"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Resource Tax + CIT + Special Oil Gain Levy",
      "royalties": "None (Replaced by 6% Resource Tax on gross crude sales).",
      "pptCit": "25% Corporate Income Tax (CIT).",
      "petroleumSpecificTax": "Special Oil Gain Levy (Progressive windfall tax 20%-40% when Brent exceeds $65/bbl).",
      "signatureBonus": "None",
      "contractModel": "Production Sharing Contract (PSC) / Mixed",
      "whoPays": "Operators under PSC / NOC JVs",
      "costRecoveryRules": "PSC cost-recovery oil provisions for foreign offshore operators.",
      "estStateRevenueCapture": "Resource Tax + CIT + Special Oil Gain Levy",
      "realTaxPrice": "Upstream: ~$9.78/bbl (@ $83/bbl)",
      "investmentIncentives": "Tax exemptions for unconventional tight oil, shale gas, and deepwater E&P.",
      "comprehensiveTaxSchedule": "Upstream: 6% Resource Tax + 25% CIT + Windfall Levy | Downstream: 1.52 RMB/L Excise + 13% VAT."
    },

    "riskManagement": {
      "hseCompliance": "Ministry of Ecology & Environment strict industrial pollution checks.",
      "financialRiskRevenueStabilization": "NDRC 10-day price ceiling buffers domestic economy against crude volatility.",
      "geopoliticalLocalContent": "Cross-border pipeline diversification (Russia, Kazakhstan, Myanmar) to bypass Malacca chokepoint.",
      "climateEnergyTransition": "Accelerated EV adoption & green hydrogen transition to peak carbon by 2030."
    },

    "transferabilityToCambodia": "Implementing dynamic retail price ceiling formulas to protect domestic markets during global price shocks.",

    "keyInstitutions": "NEA, NDRC, Ministry of Natural Resources",
    "keyDocument": "CNPC Annual Report 2024",
    "references": [
      "14th Five-Year Energy Plan of China",
      "Mineral Resources Law of the PRC",
      "CNPC / Sinopec Annual Reports 2024"
    ],
    "sources": [
      { "name": "NDRC Policy Portal", "url": "https://en.ndrc.gov.cn/policies/" },
      { "name": "EIA China Brief", "url": "https://www.eia.gov/international/analysis/country/CHN" },
      { "name": "IEA China Profile", "url": "https://www.iea.org/countries/china" }
    ]
  },

  {
    "id": "brazil",
    "country": "Brazil",
    "rank": 15,
    "tradeStatus": "Both",
    "regulatoryAuthority": "ANP / PPSA",
    "resourceOwnership": "Federal Ownership",
    "upstreamModel": "Concession & PSA",

    "oilReserveSpr": {
      "provenReserves": "~14 Billion bbls (Rank #15)",
      "provenReservesNumeric": 14,
      "sprCapacity": "30-40 Days operational storage",
      "ownershipModel": "Federal Union Ownership (ANP / PPSA)",
      "licensingModel": "Dual System: Concession (Post-Salt) & PSA (Pre-Salt)",
      "stockDuration": "30-40 days operational commercial stock managed by Petrobras & Vibra",
      "infrastructureMaintenance": "Petrobras Santos Basin FPSO fleet & Angra dos Reis marine crude storage terminal.",
      "releaseTriggers": "Operational FPSO offloading bottlenecks and domestic refinery maintenance."
    },

    "upstreamPolicy": {
      "primaryPolicyFramework": "Petroleum Law & Pre-Salt PSA Law",
      "policyYearValidity": "1997 & 2010 (Active Framework 2026)",
      "explorationLicensing": "ANP bidding rounds: Concession model for post-salt/onshore; Production Sharing (PSA) for strategic Pre-Salt poligon.",
      "roleOfNoc": "Petrobras dominates ultra-deepwater production; PPSA manages the state's profit oil share in Pre-Salt PSAs.",
      "resourceConservation": "Strict ANP unitization rules for shared reservoirs and subsea gas reinjection."
    },

    "downstreamPolicy": {
      "refiningPipelineInfra": "Refining capacity expanding (Abreu e Lima, REDUC); extensive coastal tanker shipping network.",
      "retailPricingSubsidy": "Import Parity Pricing (IPP) flexible policy; high biofuel blending mandates (E30 Ethanol, B14 Biodiesel).",
      "fuelQualityEnvStandards": "PROCONVE fuel emissions standards; RenovaBio carbon credit (CBIO) market.",
      "importDuty": "Varies (Subject to temporary tariff zeroing)",
      "exciseTax": "Federal (PIS/COFINS/CIDE): ~0.68 BRL/L",
      "vatGst": "ICMS (State Tax): Fixed ~1.22 BRL/L",
      "carbonTax": "None (RenovaBio issues tradeable CBIO carbon credits)",
      "priceRegulation": "Mixed (Petrobras sets wholesale; liberalized retail)",
      "taxCollectedBy": "Receita Federal / ANP"
    },

    "taxFiscalRegime": {
      "primaryFiscalInstruments": "Royalty + Profit Oil + Special Participation",
      "royalties": "Concession: 10%; Pre-Salt PSA: 15% fixed royalty.",
      "pptCit": "34% Corporate Income Tax (25% IRPJ + 9% CSLL).",
      "petroleumSpecificTax": "Special Participation Tax (up to 40% on high-volume profitable fields).",
      "signatureBonus": "Required (Bidding round signing bonuses)",
      "contractModel": "Mixed (Concession & PSA)",
      "whoPays": "Concessionaires / PSA consortia",
      "costRecoveryRules": "Cost Oil recovery caps in PSAs before profit oil splitting with state manager PPSA.",
      "estStateRevenueCapture": "Royalty + Profit Oil + Special Participation",
      "realTaxPrice": "Total State Capture: 65% to 70% of asset value (@ $83/bbl)",
      "investmentIncentives": "REPETRO tax suspension regime for offshore E&P capital equipment imports.",
      "comprehensiveTaxSchedule": "Upstream: 10-15% Royalty + 34% CIT + Special Participation | Downstream: ICMS (1.22 BRL/L) + Federal CIDE."
    },

    "riskManagement": {
      "hseCompliance": "IBAMA stringent environmental licensing for deepwater drilling & Santos basin FPSOs.",
      "financialRiskRevenueStabilization": "Petrobras dividend policy & state profit oil monetization via PPSA.",
      "geopoliticalLocalContent": "ANP local content requirements for subsea equipment & FPSO hull construction.",
      "climateEnergyTransition": "World leader in bioenergy integration; Petrobras investing in offshore wind & biorefineries."
    },

    "transferabilityToCambodia": "Different fiscal regimes (Concession vs PSA) may be appropriate for conventional and strategically important petroleum resources.",

    "keyInstitutions": "ANP, PPSA, Petrobras",
    "keyDocument": "ANP Annual Exploration Report 2024",
    "references": [
      "ANP Annual Exploration Report 2024",
      "Brazilian Petroleum Law (Law 9.478/1997)",
      "Pre-Salt Production Sharing Law (Law 12.351/2010)"
    ],
    "sources": [
      { "name": "ANP Govt Portal", "url": "https://www.gov.br/anp" },
      { "name": "Petrobras Portal", "url": "https://petrobras.com.br/en" },
      { "name": "EIA Brazil Brief", "url": "https://www.eia.gov/international/analysis/country/BRA" }
    ]
  }
];

# Write output to petroleum_data.js
js_file_content = f"// Comprehensive Global Petroleum Benchmark Dataset with Detailed Policy, Fiscal & Reference Taxonomy\nexport const petroleumData = {json.dumps(complete_dataset, indent=2, ensure_ascii=False)};\n"

with open('petroleum_data.js', 'w', encoding='utf-8') as f:
    f.write(js_file_content)

print(f"Successfully generated petroleum_data.js with {len(complete_dataset)} complete benchmark country records!")
