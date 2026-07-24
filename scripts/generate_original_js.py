import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('extracted_data.json', 'r', encoding='utf-8') as f:
    ext_data = json.load(f)

# Define full data for all 11 countries matching the exact original JS schema
countries = [
  {
    "id": "venezuela",
    "country": "Venezuela",
    "rank": 1,
    "tradeStatus": "Net Exporter",
    "oilReserveSpr": {
      "provenReserves": "~300-303 Billion bbls (Rank #1)",
      "provenReservesNumeric": 303,
      "sprCapacity": "Not Publicly Disclosed (Constrained operational storage)",
      "ownershipModel": "State Ownership (Ministry of Petroleum)",
      "licensingModel": "Majority State JV (PDVSA 60% mandatory majority)",
      "stockDuration": "Constrained operational storage duration due to maintenance gaps",
      "infrastructureMaintenance": "Severe maintenance gaps; aging tank farms & export terminal infrastructure.",
      "releaseTriggers": "Domestic refinery outages & severe economic supply bottlenecks."
    },
    "upstreamPolicy": {
      "explorationLicensing": "Mandatory PDVSA majority (minimum 60%) in all Empresas Mixtas joint ventures under Organic Hydrocarbons Law 2001.",
      "roleOfNoc": "Monopolistic state entity (PDVSA) manages operations; severely constrained by underinvestment and OFAC sanctions.",
      "resourceConservation": "Production capacity constrained; aging infrastructure increases environmental and operational risks."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Collapsed domestic refining sector operating far below installed capacity; severe refined fuel import deficits.",
      "retailPricingSubsidy": "Dual-market retail pricing (heavily subsidized national quota vs. international USD pricing bands).",
      "fuelQualityEnvStandards": "Reduced refining compliance; high flaring rates and lack of modern sulfur-recovery infrastructure."
    },
    "taxFiscalRegime": {
      "royalties": "33.33% statutory royalty (can reduce to 20% or lower for mature heavy oil fields).",
      "pptCit": "50% Hydrocarbon Extraction Tax + Windfall Taxes on crude exports.",
      "costRecoveryRules": "Contract & fiscal flexibility introduced under new emergency energy regulations to attract capital.",
      "investmentIncentives": "Flexible JV terms offered to foreign partners willing to commit CapEx for field rehabilitation.",
      "comprehensiveTaxSchedule": "Upstream: 33.33% Royalty + 50% CIT | Downstream: 16% VAT (collected by SENIAT) & dual quota pricing."
    },
    "riskManagement": {
      "hseCompliance": "Aging infrastructure and reduced refining capacity increase operational and environmental risks.",
      "financialRiskRevenueStabilization": "Sovereign default and OFAC sanctions hamper international crude sales and state revenues.",
      "geopoliticalLocalContent": "High reliance on imported heavy crude diluents; FONDEN social development fund contributions.",
      "climateEnergyTransition": "Minimal transition focus; immediate priority remains basic field rehabilitation and oil stabilization."
    },
    "transferabilityToCambodia": "Macroeconomic stability is essential; rigid petroleum policies struggle if the underlying state economy is unstable.",
    "references": [
      "OPEC Annual Statistical Bulletin 2024 (Venezuela Data)",
      "Organic Hydrocarbons Law of Venezuela (2001, Amended)",
      "EIA Venezuela Country Analysis Brief"
    ]
  },
  {
    "id": "saudi-arabia",
    "country": "Saudi Arabia",
    "rank": 2,
    "tradeStatus": "Net Exporter",
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
      "explorationLicensing": "Restricted state concession granted exclusively to Saudi Aramco under Hydrocarbon Law.",
      "roleOfNoc": "Monopolistic state entity (Saudi Aramco) manages 100% of crude exploration, drilling, production, and field development.",
      "resourceConservation": "Strict Maximum Sustainable Capacity (MSC) caps at ~12M bpd; aggressive water-injection & reservoir pressure maintenance."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Massive domestic refining capacity + East-West Pipeline (5M bpd) bypassing the Strait of Hormuz to Yanbu on the Red Sea.",
      "retailPricingSubsidy": "Domestic fuel retail prices regulated and linked to global price bands under fiscal reform policies.",
      "fuelQualityEnvStandards": "Transitioning domestic transport fuel to Euro V / Saudi SASO ultra-low sulfur specifications."
    },
    "taxFiscalRegime": {
      "royalties": "15% to 45% Brent-linked progressive sliding-scale royalty on gross production.",
      "pptCit": "50% Corporate Income Tax (CIT) on hydrocarbon extraction activities.",
      "costRecoveryRules": "Aramco absorbs operational and capital expenditure directly; net dividends transferred to state.",
      "investmentIncentives": "Aramco retains CapEx allocation for MSC maintenance & chemical integration.",
      "comprehensiveTaxSchedule": "Upstream: 15-45% Royalty + 50% CIT | Downstream: 15% VAT collected by ZATCA."
    },
    "riskManagement": {
      "hseCompliance": "Strict internal Aramco environmental & safety standards; zero routine flaring target by 2030.",
      "financialRiskRevenueStabilization": "OPEC+ production quota leadership stabilizes global Brent crude price; Public Investment Fund (PIF) diversifies national wealth.",
      "geopoliticalLocalContent": "East-West Pipeline mitigates Strait of Hormuz blockade risk; iktva program mandates >70% local content procurement.",
      "climateEnergyTransition": "Major investments in CCUS (Carbon Capture), green hydrogen, and solar power integration at extraction fields."
    },
    "transferabilityToCambodia": "Strategic infrastructure investment (bypass pipelines) and establishing a state-directed buffer to secure national energy supply.",
    "references": [
      "Saudi Aramco Annual Report 2024",
      "Law of Petroleum and Petrochemical Products (Royal Decree M/37)",
      "Saudi Vision 2030 Energy Framework"
    ]
  },
  {
    "id": "iran",
    "country": "Iran",
    "rank": 3,
    "tradeStatus": "Net Exporter",
    "oilReserveSpr": {
      "provenReserves": "~208 Billion bbls (Rank #3)",
      "provenReservesNumeric": 208,
      "sprCapacity": "~71 Million bbls floating storage",
      "ownershipModel": "State Ownership (Ministry of Petroleum / NIOC)",
      "licensingModel": "Risk Service Contract (Iran Petroleum Contract - IPC)",
      "stockDuration": "Floating operational buffer on offshore VLCC tankers",
      "infrastructureMaintenance": "NITC (National Iranian Tanker Co.) floating storage fleet and Kharg Island export terminal.",
      "releaseTriggers": "Sanctions avoidance logistics & international market export windows."
    },
    "upstreamPolicy": {
      "explorationLicensing": "NIOC absolute monopoly; foreign entry restricted to IPC risk-service contracts with no resource equity.",
      "roleOfNoc": "NIOC (National Iranian Oil Co.) retains 100% resource ownership & field operation rights.",
      "resourceConservation": "Production constrained by sanctions and lack of modern gas-reinjection EOR technology."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Large domestic refining capacity focusing on domestic gasoline self-sufficiency.",
      "retailPricingSubsidy": "Extensive domestic retail subsidies leading to high cross-border fuel smuggling rates.",
      "fuelQualityEnvStandards": "Euro IV / V transition slow due to equipment import restrictions under trade sanctions."
    },
    "taxFiscalRegime": {
      "royalties": "None (No traditional concession royalty under constitution).",
      "pptCit": "25% CIT for foreign entities under IPC cost recovery framework.",
      "costRecoveryRules": "Approved OPEX & CAPEX recovery plus a fixed fee per barrel for foreign contractors.",
      "investmentIncentives": "Higher remuneration fees offered for technically challenging offshore & EOR fields.",
      "comprehensiveTaxSchedule": "Upstream: IPC Service Fee + 25% CIT | Downstream: 9% VAT + 1% Green Tax (INTA)."
    },
    "riskManagement": {
      "hseCompliance": "Aging offshore platforms & refineries limit HSE compliance.",
      "financialRiskRevenueStabilization": "Subsidies strain national budget; high exposure to sanctions & international financial restrictions.",
      "geopoliticalLocalContent": "Goreh-Jask pipeline constructed to bypass Strait of Hormuz to the Gulf of Oman.",
      "climateEnergyTransition": "High gas flaring rates; renewable energy initiatives under-resourced."
    },
    "transferabilityToCambodia": "Fuel subsidy reforms should balance social affordability with fiscal sustainability.",
    "references": [
      "OPEC Annual Statistical Bulletin 2024 (Iran Data)",
      "Petroleum Act of Iran (1987, Amended 2016)",
      "Iran Petroleum Contract (IPC) Framework"
    ]
  },
  {
    "id": "canada",
    "country": "Canada",
    "rank": 4,
    "tradeStatus": "Both",
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
      "explorationLicensing": "Provincial Crown land tenure auctions governed by AER (Alberta) and Ministry of Energy.",
      "roleOfNoc": "No National Oil Company (NOC); private commercial oil sands and conventional producers.",
      "resourceConservation": "Strict oil sands tailings management, SAGD reservoir optimization, and provincial carbon emissions limits."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Trans Mountain Expansion (TMX) pipeline (890k bpd) opens Pacific export routes; extensive crude-by-rail backup.",
      "retailPricingSubsidy": "Free-market pricing governed by transparent market competition; carbon tax transparently added to pump price.",
      "fuelQualityEnvStandards": "Federal Clean Fuel Regulations (CFR) requiring carbon intensity reductions across fuel suppliers."
    },
    "taxFiscalRegime": {
      "royalties": "Sliding-scale royalty based on project payout (Alberta: 1%-9% pre-payout, 25%-40% post-payout based on WTI price).",
      "pptCit": "Combined Federal (15%) + Provincial (8%-12%) CIT total ~23-27%.",
      "costRecoveryRules": "Low pre-payout royalties accelerate CapEx write-off before higher post-payout rates apply.",
      "investmentIncentives": "CapEx write-offs & clean technology investment tax credits (CCUS).",
      "comprehensiveTaxSchedule": "Upstream: 1-40% Royalty + ~23% CIT | Downstream: Federal Excise ($0.10/L) + Carbon Tax + GST (CRA)."
    },
    "riskManagement": {
      "hseCompliance": "Strict AER environmental oversight & oil sands monitoring programs.",
      "financialRiskRevenueStabilization": "Alberta Heritage Savings Trust Fund manages fiscal price volatility.",
      "geopoliticalLocalContent": "TMX pipeline mitigates reliance on US Gulf Coast market buyers.",
      "climateEnergyTransition": "Federal 2030 Emissions Reduction Plan and Pathways Alliance oil sands net-zero initiative."
    },
    "transferabilityToCambodia": "A petroleum stabilization fund (like Alberta Heritage Fund) could help reduce fiscal volatility.",
    "references": [
      "CER Annual Report of the Commission 2023-24",
      "Alberta Energy Regulator (AER) Directives",
      "Canadian Energy Regulator (CER) Act"
    ]
  },
  {
    "id": "iraq",
    "country": "Iraq",
    "rank": 5,
    "tradeStatus": "Net Exporter",
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
      "explorationLicensing": "Federal TSCs via licensing rounds; KRG utilizes Production Sharing Agreements (PSAs).",
      "roleOfNoc": "State Oil Companies (Basra Oil Co., North Oil Co., SOMO) maintain 100% resource title & mandatory 25% state partner equity.",
      "resourceConservation": "Major common seawater supply project (CSSP) needed for reservoir pressure maintenance in giant southern fields."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Karbala & Baiji refineries expanded to reduce fuel import reliance; Ceyhan export pipeline currently stalled.",
      "retailPricingSubsidy": "Heavy state retail fuel subsidies; inland storage prioritized for domestic power generation.",
      "fuelQualityEnvStandards": "Upgrading domestic refining slate to reduce heavy fuel oil surplus and meet Euro V standards."
    },
    "taxFiscalRegime": {
      "royalties": "None federally (10% under KRG PSAs).",
      "pptCit": "35% CIT on foreign contractor remuneration fees.",
      "costRecoveryRules": "IOCs recover 100% of approved OPEX & CAPEX plus fixed fee per barrel.",
      "investmentIncentives": "Remuneration fee indexation and rapid cost recovery provisions.",
      "comprehensiveTaxSchedule": "Upstream: Fixed TSC Remuneration Fee ($1.50-$5.50/bbl) + 35% CIT | Downstream: Subsidized pump pricing."
    },
    "riskManagement": {
      "hseCompliance": "High security protection investments required; flaring reduction programs underway with TotalEnergies.",
      "financialRiskRevenueStabilization": "Federal government budget heavily exposed to crude price swings; oil revenues fund state payroll.",
      "geopoliticalLocalContent": "Vulnerability due to Federal vs KRG regulatory disputes and Strait of Hormuz transit dependence.",
      "climateEnergyTransition": "Gas growth project aimed at capturing flared gas for domestic electricity generation."
    },
    "transferabilityToCambodia": "Technical Service Contracts (TSCs) could be considered to maintain sovereign ownership over resources.",
    "references": [
      "Iraq EITI Report 2024",
      "Draft Federal Oil and Gas Law of Iraq (2007)",
      "EIA Iraq Country Analysis Brief"
    ]
  },
  {
    "id": "united-arab-emirates",
    "country": "United Arab Emirates",
    "rank": 6,
    "tradeStatus": "Net Exporter",
    "oilReserveSpr": {
      "provenReserves": "~113 Billion bbls (Rank #6)",
      "provenReservesNumeric": 113,
      "sprCapacity": "~34 Million bbls on-land storage",
      "ownershipModel": "State Ownership (Abu Dhabi Supreme Council for Financial & Economic Affairs)",
      "licensingModel": "Majority State JV (ADNOC mandates 60% majority equity)",
      "stockDuration": "Strategic commercial & operational buffer at Port of Fujairah",
      "infrastructureMaintenance": "Fujairah deepwater terminal & tank farm hub with continuous expansion.",
      "releaseTriggers": "Commercial market arbitrage & Gulf export security emergencies."
    },
    "upstreamPolicy": {
      "explorationLicensing": "Competitive concession bidding rounds; ADNOC is mandatory majority partner (60%) in all concessions.",
      "roleOfNoc": "ADNOC (Abu Dhabi National Oil Co.) manages production targets & maximum sustainable capacity increases to 5M bpd by 2027.",
      "resourceConservation": "Industry-leading zero routine flaring target and extensive CCUS implementation in offshore fields."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Ruwais mega-refining complex + ADCOP pipeline (1.5M bpd) pumping crude directly to Fujairah outside the Strait of Hormuz.",
      "retailPricingSubsidy": "Fully liberalized retail pricing tied to international monthly benchmarks since 2015.",
      "fuelQualityEnvStandards": "Strict Euro V transport fuel standards; green hydrogen & SAF aviation fuel investments."
    },
    "taxFiscalRegime": {
      "royalties": "Base royalty on gross production (~20% concession-specific).",
      "pptCit": "55% to 85% Upstream Corporate Income Tax on foreign concession partners.",
      "costRecoveryRules": "Proportionate OPEX & CAPEX recovery before tax calculation.",
      "investmentIncentives": "In-Country Value (ICV) certification grants preferred status in CapEx procurement.",
      "comprehensiveTaxSchedule": "Upstream: ~20% Royalty + 55-85% CIT | Downstream: 5% VAT collected by FTA."
    },
    "riskManagement": {
      "hseCompliance": "ADNOC stringent HSE policy framework; zero-flaring & decarbonization targets.",
      "financialRiskRevenueStabilization": "Abu Dhabi Investment Authority (ADIA) sovereign fund absorbs oil price cycles.",
      "geopoliticalLocalContent": "ADCOP pipeline bypasses Strait of Hormuz to Fujairah; ICV program mandates local procurement.",
      "climateEnergyTransition": "UAE Energy Strategy 2050 targets net-zero by 2050 with $54B renewable energy commitment."
    },
    "transferabilityToCambodia": "Mandating NOC participation in joint ventures ensures technology transfer and state oversight.",
    "references": [
      "UAE Energy Strategy 2050 (Updated 2023)",
      "ADNOC In-Country Value (ICV) Program Guidelines",
      "Ministry of Energy and Infrastructure Directives"
    ]
  },
  {
    "id": "kuwait",
    "country": "Kuwait",
    "rank": 7,
    "tradeStatus": "Net Exporter",
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
      "explorationLicensing": "Absolute state monopoly; constitutional prohibition of foreign resource ownership or concessions.",
      "roleOfNoc": "KPC (Kuwait Petroleum Corp) & KOC (Kuwait Oil Co.) manage 100% of crude exploration & production.",
      "resourceConservation": "Managing pressure depletion in the massive Burgan field via advanced water injection."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Al-Zour mega-refinery (615k bpd) producing clean low-sulfur fuel oil for domestic power & export.",
      "retailPricingSubsidy": "Heavily subsidized domestic fuel and electricity pricing.",
      "fuelQualityEnvStandards": "Clean Fuels Project completed; domestic & export refining upgraded to Euro V ultra-low sulfur standards."
    },
    "taxFiscalRegime": {
      "royalties": "None (100% state resource ownership).",
      "pptCit": "15% CIT (Applies only to foreign contractor service fees; KPC/KOC exempt).",
      "costRecoveryRules": "Contractors paid fixed service fees & incentive bonuses; no crude ownership.",
      "investmentIncentives": "Performance-based incentive bonuses for enhanced heavy oil recovery.",
      "comprehensiveTaxSchedule": "Upstream: 100% State Net Rent | Downstream: Subsidized retail prices (Ministry of Finance)."
    },
    "riskManagement": {
      "hseCompliance": "KOC rigorous HSE management system; lowering gas flaring below 1%.",
      "financialRiskRevenueStabilization": "Kuwait Investment Authority (KIA) Sovereign Wealth Fund mitigates long-term oil price shocks.",
      "geopoliticalLocalContent": "High strategic reliance on the Strait of Hormuz for export logistics.",
      "climateEnergyTransition": "KPC 2050 Decarbonization Strategy targeting net-zero Scope 1 & 2 emissions."
    },
    "transferabilityToCambodia": "Technical Service Agreements (TSAs) can facilitate technology acquisition without ceding equity.",
    "references": [
      "KPC Strategy 2040",
      "Law No. 6 of 1980 Establishing Kuwait Petroleum Corporation",
      "EIA Kuwait Country Analysis Brief"
    ]
  },
  {
    "id": "russia",
    "country": "Russia",
    "rank": 8,
    "tradeStatus": "Net Exporter",
    "oilReserveSpr": {
      "provenReserves": "~80 Billion bbls (Rank #8)",
      "provenReservesNumeric": 80,
      "sprCapacity": "Not Publicly Disclosed (Continuous Transneft pipeline float)",
      "ownershipModel": "State Subsoil Ownership (Minenergo / Rosnedra)",
      "licensingModel": "Subsoil Licensing / Majority State JV (Rosneft, Gazprom Neft)",
      "stockDuration": "Continuous logistical float across Transneft trunk pipeline grid",
      "infrastructureMaintenance": "Transneft pipeline network (>50,000 km) and Baltic / Pacific port terminals (Primorsk, Kozmino).",
      "releaseTriggers": "Export reorientation logistics & refinery maintenance scheduling."
    },
    "upstreamPolicy": {
      "explorationLicensing": "Subsoil auctions managed by Rosnedra; strategic offshore & Arctic fields restricted to state NOCs.",
      "roleOfNoc": "State-backed NOCs (Rosneft, Gazprom Neft) dominate crude extraction.",
      "resourceConservation": "Optimizing extraction from mature Western Siberian fields via horizontal drilling and hydrofracking."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Complete reorientation of crude export logistics from Europe toward China & India via ESPO pipeline and dark fleet tankers.",
      "retailPricingSubsidy": "Government intervention via the Damper Mechanism to subsidize domestic refineries & cap pump prices.",
      "fuelQualityEnvStandards": "GOST / Technical Regulations (Euro 5 equivalent domestic standards)."
    },
    "taxFiscalRegime": {
      "royalties": "None (Replaced by NDPI - Mineral Extraction Tax tied to Urals price formula).",
      "pptCit": "25% CIT (Effective 2025 tax code amendment).",
      "costRecoveryRules": "Limited cost recovery under NDPI; NDD provides profit-based tax relief for greenfield projects.",
      "investmentIncentives": "NDD profit-based tax regime applied to Eastern Siberia and Arctic greenfield developments.",
      "comprehensiveTaxSchedule": "Upstream: NDPI (Extraction Tax) + NDD (Additional Income Tax) + 25% CIT | Downstream: 20% VAT (MinFin)."
    },
    "riskManagement": {
      "hseCompliance": "Rostekhnadzor industrial safety & environmental oversight.",
      "financialRiskRevenueStabilization": "Damper mechanism stabilizes domestic retail fuel prices regardless of global Brent/Urals swings.",
      "geopoliticalLocalContent": "Western sanctions mitigation via alternative maritime logistics and shadow tanker fleets.",
      "climateEnergyTransition": "Energy Strategy 2035 prioritizes maintaining global crude market share."
    },
    "transferabilityToCambodia": "Ensuring fiscal policies secure immediate state revenues from resource extraction.",
    "references": [
      "Energy Strategy of the Russian Federation to 2035",
      "Law of the Russian Federation on Subsoil (1992)",
      "Tax Code of the Russian Federation (NDPI/NDD Amendments)"
    ]
  },
  {
    "id": "united-states",
    "country": "United States",
    "rank": 11,
    "tradeStatus": "Both",
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
      "explorationLicensing": "Decentralized leasing via BOEM (offshore) and BLM (onshore); private landowners lease mineral rights directly to operators.",
      "roleOfNoc": "No National Oil Company (NOC); 100% private IOC and independent commercial oil & gas operators.",
      "resourceConservation": "State regulatory commissions (e.g. Texas Railroad Commission) enforce well spacing, anti-flaring rules, and allowable production rates."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Largest refining capacity globally (Gulf Coast hubs) linked via Colonial & Enbridge pipeline networks.",
      "retailPricingSubsidy": "100% free-market liberalized retail pricing determined by market competition without state subsidies.",
      "fuelQualityEnvStandards": "Strict EPA Clean Air Act Tier 3 gasoline sulfur limits & Renewable Fuel Standard (RFS) ethanol blending mandates."
    },
    "taxFiscalRegime": {
      "royalties": "Federal Onshore: 16.67%; Federal Offshore: 12.5% to 18.75%; Private/State royalties vary (12.5%-25%).",
      "pptCit": "Federal CIT: 21% + State Corporate Income Tax (0%-12%).",
      "costRecoveryRules": "Intangible Drilling Costs (IDC) full immediate tax write-offs & percentage depletion allowances.",
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
    "references": [
      "DOE FY 2024 Annual Performance Report",
      "US Energy Policy Act & Inflation Reduction Act (IRA)",
      "BOEM/BSEE Outer Continental Shelf Lands Act Regulations"
    ]
  },
  {
    "id": "china",
    "country": "China",
    "rank": 13,
    "tradeStatus": "Both",
    "oilReserveSpr": {
      "provenReserves": "~26 Billion bbls (Rank #13)",
      "provenReservesNumeric": 26,
      "sprCapacity": "~1.3 - 1.4 Billion bbls combined",
      "ownershipModel": "State Ownership (Ministry of Natural Resources)",
      "licensingModel": "Production Sharing Contract (PSC) / State NOC Monopoly",
      "stockDuration": "~90-100 days import protection buffer across national SPR bases",
      "infrastructureMaintenance": "State-owned strategic reserve bases (Zhoushan, Zhenhai, Dalian, Qingdao) & CNPC/Sinopec commercial tank farms.",
      "releaseTriggers": "NDRC macroeconomic price ceiling enforcement & international supply disruption mitigation."
    },
    "upstreamPolicy": {
      "explorationLicensing": "NOCs (CNPC, Sinopec, CNOOC) dominate acreage; foreign entry allowed primarily through PSC joint ventures.",
      "roleOfNoc": "State NOCs control >90% of domestic exploration & production.",
      "resourceConservation": "High priority on Enhanced Oil Recovery (EOR), polymer flooding (Daqing field), and deepwater South China Sea exploration."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "World-class refining capacity (Teapot refiners + Sinopec mega-hubs) + Russia ESPO & Central Asia import pipelines.",
      "retailPricingSubsidy": "NDRC adjusts domestic refined fuel prices every 10 working days based on global crude price bands (floor $40, ceiling $130).",
      "fuelQualityEnvStandards": "National VI (Euro 6 equivalent) gasoline & diesel emissions standards nationwide."
    },
    "taxFiscalRegime": {
      "royalties": "None (Replaced by 6% Resource Tax on gross crude sales).",
      "pptCit": "25% Corporate Income Tax (CIT).",
      "costRecoveryRules": "PSC cost-recovery oil provisions for foreign offshore operators.",
      "investmentIncentives": "Tax exemptions for unconventional tight oil, shale gas, and deepwater E&P.",
      "comprehensiveTaxSchedule": "Upstream: 6% Resource Tax + 25% CIT + Special Oil Gain Levy | Downstream: 1.52 RMB/L Excise + 13% VAT."
    },
    "riskManagement": {
      "hseCompliance": "Ministry of Ecology & Environment strict industrial pollution checks.",
      "financialRiskRevenueStabilization": "NDRC 10-day price ceiling buffers domestic economy against crude volatility.",
      "geopoliticalLocalContent": "Cross-border pipeline diversification (Russia, Kazakhstan, Myanmar) to bypass Malacca chokepoint.",
      "climateEnergyTransition": "Accelerated EV adoption & green hydrogen transition to peak carbon by 2030."
    },
    "transferabilityToCambodia": "Implementing dynamic retail price ceilings to protect domestic markets during global price shocks.",
    "references": [
      "CNPC Annual Report 2024",
      "14th Five-Year Energy Plan of China",
      "Mineral Resources Law of the PRC"
    ]
  },
  {
    "id": "brazil",
    "country": "Brazil",
    "rank": 15,
    "tradeStatus": "Both",
    "oilReserveSpr": {
      "provenReserves": "~14 Billion bbls (Rank #15)",
      "provenReservesNumeric": 14,
      "sprCapacity": "30-40 Days operational storage",
      "ownershipModel": "Federal Ownership (ANP / PPSA)",
      "licensingModel": "Concession & PSA (Dual System)",
      "stockDuration": "30-40 days operational commercial stock managed by Petrobras & Vibra",
      "infrastructureMaintenance": "Petrobras Santos Basin FPSO fleet & Angra dos Reis marine crude storage terminal.",
      "releaseTriggers": "Operational FPSO offloading bottlenecks and domestic refinery maintenance."
    },
    "upstreamPolicy": {
      "explorationLicensing": "ANP bidding rounds: Concession model for post-salt/onshore; Production Sharing (PSA) for strategic Pre-Salt polygon.",
      "roleOfNoc": "Petrobras dominates ultra-deepwater production; PPSA manages the state's profit oil share in Pre-Salt PSAs.",
      "resourceConservation": "Strict ANP unitization rules for shared reservoirs and subsea gas reinjection."
    },
    "downstreamPolicy": {
      "refiningPipelineInfra": "Refining capacity expanding (Abreu e Lima, REDUC); extensive coastal tanker shipping network.",
      "retailPricingSubsidy": "Mixed pricing with periodic state intervention; high biofuel blending mandates (E30 Ethanol, B14 Biodiesel).",
      "fuelQualityEnvStandards": "PROCONVE fuel emissions standards; RenovaBio carbon credit (CBIO) market."
    },
    "taxFiscalRegime": {
      "royalties": "Concession: 10%; Pre-Salt PSA: 15% fixed royalty.",
      "pptCit": "34% Corporate Income Tax (25% IRPJ + 9% CSLL).",
      "costRecoveryRules": "Cost Oil recovery caps in PSAs before profit oil splitting with state manager PPSA.",
      "investmentIncentives": "REPETRO tax suspension regime for offshore E&P capital equipment imports.",
      "comprehensiveTaxSchedule": "Upstream: 10-15% Royalty + 34% CIT + Special Participation Tax (up to 40%) | Downstream: ICMS (1.22 BRL/L) + CIDE."
    },
    "riskManagement": {
      "hseCompliance": "IBAMA stringent environmental licensing for deepwater drilling & Santos basin FPSOs.",
      "financialRiskRevenueStabilization": "State intervention in Petrobras wholesale pricing & profit oil monetization via PPSA.",
      "geopoliticalLocalContent": "ANP local content requirements for subsea equipment & FPSO hull construction.",
      "climateEnergyTransition": "Different fiscal regimes may be appropriate for conventional and strategically important petroleum resources."
    },
    "transferabilityToCambodia": "Different fiscal regimes may be appropriate for conventional and strategically important petroleum resources.",
    "references": [
      "ANP Annual Exploration Report 2024 (Relatório Anual de Exploração)",
      "Petroleum Law of Brazil (Law 9.478/1997)",
      "Pre-Salt Production Sharing Law (Law 12.351/2010)"
    ]
  }
]

# Generate JavaScript formatted string
js_code = "// Comprehensive Global Petroleum Benchmark Dataset with Detailed Policy & Fiscal Taxonomy\nexport const petroleumData = [\n"

for i, c in enumerate(countries):
    js_code += "  {\n"
    js_code += f'    id: "{c["id"]}",\n'
    js_code += f'    country: "{c["country"]}",\n'
    js_code += f'    rank: {c["rank"]},\n'
    js_code += f'    tradeStatus: "{c["tradeStatus"]}",\n\n'
    
    js_code += "    // 1. Oil Reserve Ranking & SPR\n"
    js_code += "    oilReserveSpr: {\n"
    for k, v in c["oilReserveSpr"].items():
        if isinstance(v, (int, float)):
            js_code += f'      {k}: {v},\n'
        else:
            js_code += f'      {k}: "{v}",\n'
    js_code = js_code.rstrip(",\n") + "\n    },\n\n"

    js_code += "    // 2. Upstream Policy\n"
    js_code += "    upstreamPolicy: {\n"
    for k, v in c["upstreamPolicy"].items():
        js_code += f'      {k}: "{v}",\n'
    js_code = js_code.rstrip(",\n") + "\n    },\n\n"

    js_code += "    // 3. Downstream Policy\n"
    js_code += "    downstreamPolicy: {\n"
    for k, v in c["downstreamPolicy"].items():
        js_code += f'      {k}: "{v}",\n'
    js_code = js_code.rstrip(",\n") + "\n    },\n\n"

    js_code += "    // 4. Tax (Fiscal Regime)\n"
    js_code += "    taxFiscalRegime: {\n"
    for k, v in c["taxFiscalRegime"].items():
        js_code += f'      {k}: "{v}",\n'
    js_code = js_code.rstrip(",\n") + "\n    },\n\n"

    js_code += "    // 5. Risk Management\n"
    js_code += "    riskManagement: {\n"
    for k, v in c["riskManagement"].items():
        js_code += f'      {k}: "{v}",\n'
    js_code = js_code.rstrip(",\n") + "\n    },\n\n"

    js_code += f'    transferabilityToCambodia: "{c["transferabilityToCambodia"]}",\n'
    js_code += '    references: [\n'
    for r in c["references"]:
        js_code += f'      "{r}",\n'
    js_code = js_code.rstrip(",\n") + "\n    ]\n"
    js_code += "  }" + (",\n" if i < len(countries)-1 else "\n")

js_code += "];\n"

with open("petroleum_data.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Successfully written petroleum_data.js in original JS object literal format!")
