import requests
import plotly.express as px

# ghoapi expectancy life api
world_healt_url = f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq 'USA' and TimeDimensionValue eq '2021' and Dim1 eq 'SEX_BTSX'"

country_code = ['AFG', 'AGO', 'ALB', 'ARE', 'ARG', 'ARM', 'ASM', 'ATG', 'AUS','AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BES', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA', 'LSO', 'LTU', 'LUX', 'LVA', 'MAC', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'ME1', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MSR', 'MTQ', 'MUS', 'MWI', 'MYS', 'MYT', 'NAM', 'NCL', 'NER', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI', 'PRK', 'PRS', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SDN736', 'SEN', 'SGP', 'SHN', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SPM', 'SRB', 'SSD', 'STP','SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SXM', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WLF', 'WSM', 'XKX', 'YEM', 'ZAF', 'ZMB', 'ZWE']


# print(len(country_code))
# data = []
data = [('AFG', 59.12690224), ('AGO', 62.13113467), ('ALB', 76.39089034), ('ARE', 78.30645695), ('ARG', 74.56898059), ('ARM', 72.98458202), ('ATG', 76.91527032), ('AUS', 83.10183853), ('AUT', 80.99297519), ('AZE', 72.9129401), ('BDI', 64.00694993), ('BEL', 81.5059627), ('BEN', 64.01268515), ('BFA', 62.29728841), ('BGD', 73.10251672), ('BGR', 71.30586), ('BHR', 74.38371772), ('BHS', 70.43274063), ('BIH', 74.84944487), ('BLR', 73.12324771), ('BLZ', 73.32055336), ('BOL', 65.41062535), ('BRA', 72.38840694), ('BRB', 76.8418344), ('BRN', 76.92260844), ('BTN', 74.87642848), ('BWA', 61.23119159), ('CAF', 52.30772755), ('CAN', 81.58276248), ('CHE', 83.32795777), ('CHL', 79.02404788), ('CHN', 77.61619672), ('CIV', 63.5174083), ('CMR', 61.76934896), ('COD', 61.62552641), ('COG', 63.17262301), ('COL', 74.53297363), ('COM', 67.4970386), ('CPV', 73.16097765), ('CRI', 78.63053412), ('CUB', 73.67333077), ('CYP', 81.912741), ('CZE', 77.07730392), ('DEU', 80.49140555), ('DJI', 64.87227149), ('DNK', 81.18400442), ('DOM', 73.32102758), ('DZA', 75.97765182), ('ECU', 73.95801182), ('EGY', 69.10821615), ('ERI', 63.57308435), ('ESP', 82.66267258), ('EST', 77.13131363), ('ETH', 67.83909086), ('FIN', 81.53419484), ('FJI', 65.50058445), ('FRA', 81.92274175), ('FSM', 65.70956674), ('GAB', 65.09380891), ('GBR', 80.10062783), ('GEO', 71.24038597), ('GHA', 66.10178519), ('GIN', 61.26251027), ('GMB', 64.21396887), ('GNB', 58.62801846), ('GNQ', 61.60542301), ('GRC', 79.59785025), ('GRD', 72.77322454), ('GTM', 68.69573697), ('GUY', 66.0777533), ('HND', 68.96309289), ('HRV', 76.8616792), ('HTI', 62.4563858), ('HUN', 74.39546955), ('IDN', 68.26167935), ('IND', 67.30780612), ('IRL', 81.60162902), ('IRN', 74.71077692), ('IRQ', 71.46632369), ('ISL', 82.57766731), ('ISR', 81.74464677), ('ITA', 82.19747411), ('JAM', 70.1439437), ('JOR', 75.64973596), ('JPN', 84.46067178), ('KAZ', 70.27511981), ('KEN', 66.76221995), ('KGZ', 72.18500345), ('KHM', 68.92399972), ('KIR', 60.87345633), ('KOR', 83.79982334), ('KWT', 78.95211671), ('LAO', 68.23189407), ('LBN', 74.34207035), ('LBR', 63.45730846), ('LBY', 72.17844009), ('LCA', 71.1130421), ('LKA', 77.22895472), ('LSO', 51.47907482), ('LTU', 74.13314711), ('LUX', 82.78028566), ('LVA', 73.20251724), ('MAR', 72.61868352), ('MDA', 69.55780877), ('MDG', 62.9342555), ('MDV', 75.39664085), ('MEX', 70.83258685), ('MKD', 72.99535604), ('MLI', 61.67398609), ('MLT', 81.81193837), ('MMR', 67.84580637), ('MNE', 74.70975149), ('MNG', 70.09795294), ('MOZ', 57.66202708), ('MRT', 68.86843813), ('MUS', 73.41967032), ('MWI', 62.48652597), ('MYS', 72.8101035), ('NAM', 60.35994599), ('NER', 59.97070525), ('NGA', 63.3974984), ('NIC', 75.02796138), ('NLD', 81.12478594), ('NOR', 82.88199872), ('NPL', 70.04936795), ('NZL', 82.20149177), ('OMN', 72.47676726), ('PAK', 65.99092295), ('PAN', 77.23869904), ('PER', 71.66727055), ('PHL', 66.40834182), ('PNG', 65.48786529), ('POL', 75.4021086), ('PRI', 79.90294803), ('PRK', 72.6431485), ('PRT', 81.17961003), ('PRY', 70.27080999), ('PSE', 73.49178033), ('QAT', 76.7101384), ('ROU', 72.76430945), ('RUS', 70.017337), ('RWA', 67.54213882), ('SAU', 76.42921259), ('SDN', 67.58515204), ('SEN', 67.79198263), ('SGP', 83.85708962), ('SLB', 64.79245685), ('SLE', 61.0228635), ('SLV', 71.66703998), ('SOM', 53.95143945), ('SRB', 72.80891574), ('SSD', 58.57353884), ('STP', 71.17810896), ('SUR', 69.78412349), ('SVK', 74.50941328), ('SVN', 80.41495666), ('SWE', 82.6649092), ('SWZ', 54.59266973), ('SYC', 74.01196664), ('SYR', 72.43803165), ('TCD', 59.08581443), ('TGO', 63.86461122), ('THA', 75.29014364), ('TJK', 71.814877), ('TKM', 69.12049331), ('TLS', 67.99671222), ('TON', 72.72088222), ('TTO', 71.70712647), ('TUN', 74.06842662), ('TUR', 75.27238945), ('TZA', 66.8101483), ('UGA', 65.98577935), ('UKR', 70.90674708), ('URY', 74.98295244), ('USA', 76.37368104), ('UZB', 72.18877681), ('VCT', 72.55709418), ('VEN', 71.22082891), ('VNM', 73.7965773), ('VUT', 66.3483713), ('WSM', 70.27372108), ('YEM', 65.76206783), ('ZAF', 61.49918805), ('ZMB', 60.96884286), ('ZWE', 58.48102238)]


# Getting all the life expectancy data from the api and store it in a local data

for i in range(len(country_code)):
    req = requests.get(f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq '{country_code[i]}' and TimeDimensionValue eq '2021' and Dim1 eq 'SEX_BTSX'")
    res = req.json()
    if not len(res['value']):
        continue
    out = res['value'][0]['NumericValue']
    data.append((country_code[i], out))

# req = requests.get(f"https://ghoapi.azureedge.net/api/WHOSIS_000001?$filter=SpatialDim eq 'ASM' and TimeDimensionValue eq '2021' and Dim1 eq 'SEX_BTSX'")
# res = req.json()
# print(res['value'])
# print(res['value'] == [])


# Showing the life expectancy data to the web with a map format

print(data)
fig = px.choropleth(data, locations=0, color=1)
fig.show()
