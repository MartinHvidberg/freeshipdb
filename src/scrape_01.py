
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#from bs4 import bs

import ship_info_extractors as sie

def extract_shipinfo(str_url, soup):
    if "vesseltracker" in str_url:
        dic_shipinfo = sie.esi_vt(r.data)
    return dic_shipinfo

# load site list
with open("sites.csv", "r") as fils:
    lst_sites = fils.readlines()

for site in lst_sites:
    site1 = [tok.strip().replace('"','') for tok in site.split(',')]
    print(" site: {}".format(site1))

    lst_targets = range(7110878, 7119999) # [7116808] #

    for mmsi in lst_targets:
        str_url = "{}{}{}{}".format(site1[0], site1[1], str(mmsi), site1[2])
        #print(str_url)

        http = urllib3.PoolManager()
        r = http.request('GET', str_url)
        if r.status == 200:
            dic_shipinfo = extract_shipinfo(str_url, r.data)
            print("mmsi: {} >> {}".format(mmsi, dic_shipinfo))
            with open('..//data//eci//'+str(mmsi)+'.eci', 'w') as filo:
                filo.write(str(dic_shipinfo))
        elif r.status == 404:
            # Page not found
            pass
        else:
            print("Request returned error: {} for {}".format(r.status, str_url))


    ###

        #with open("sample.html", "w") as fils:
        #    fils.writelines(str(r.data))