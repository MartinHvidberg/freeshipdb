
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#from bs4 import bs

import ship_info_extractors as sie

def extract_shipinfo(str_url, soup):
    if "vesseltracker" in str_url:
        dic_shipinfo = sie.esi_vt(r.data)
    return dic_shipinfo

with open("sites.csv", "r") as fils:
    lst_sites = fils.readlines()
site1 = [tok.strip().replace('"','') for tok in lst_sites[0].split(',')]
print(site1)
mmsi = 7116808
str_url = "{}{}{}{}".format(site1[0], site1[1], str(mmsi), site1[2])
print(str_url)


http = urllib3.PoolManager()
r = http.request('GET', str_url)
if r.status == 200:
    dic_shipinfo = extract_shipinfo(str_url, r.data)
    print(dic_shipinfo)
    with open(str(mmsi)+'.eci', 'w') as filo:
        filo.write(str(dic_shipinfo))
else:
    print("Request returned error: {} for {}".format(r.status, str_url))


###

    #with open("sample.html", "w") as fils:
    #    fils.writelines(str(r.data))