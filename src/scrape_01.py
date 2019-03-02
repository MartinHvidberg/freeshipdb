
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

    lst_targets = range(3000000, 3999999) # [7116808] #

    for imo in lst_targets:
        # Check IMO check-digit nnnnnnP
        str_imo = str(imo)  # then works both with int and str input
        if len(str_imo) == 7:
            try:
                il = int(str_imo[:-1])
            except ValueError:
                print("This imo seems invalid: {}".format(str_imo))
                continue
            try:
                ir = int(str_imo[-1:])
            except ValueError:
                print("This imo seems invalid: {}".format(str_imo))
                continue
            sl = str_imo[:-1]
            int_ctrl = (int(sl[0])*7
                        + int(sl[1])*6
                        + int(sl[2])*5
                        + int(sl[3])*4
                        + int(sl[4])*3
                        + int(sl[5])*2) % 10
            if ir != int_ctrl:
                continue  # Control number didn't check out, don't even try...
        else:
            print("Seems that IMO number is not 7 digits: {}".format(str_imo))

        # Build IMO search URL
        str_url = "{}{}{}{}".format(site1[0], site1[1], str(imo), site1[2])
        print("URL: {} :: {}-{}={}".format(str_url, il, ir, int_ctrl))
        http = urllib3.PoolManager()
        r = http.request('GET', str_url)
        if r.status == 200:
            dic_shipinfo = extract_shipinfo(str_url, r.data)
            print("imo: {} >> {}".format(imo, dic_shipinfo))
            with open('..//data//eci//'+str(imo)+'.eci', 'w') as filo:
                filo.write(str(dic_shipinfo))
        elif r.status == 404:
            # Page not found
            pass
        else:
            print("Request returned error: {} for {}".format(r.status, str_url))


"""
This is done by multiplying each of the first six digits by a factor of 2 to 7 corresponding to their position from right to left. The rightmost digit of this sum is the check digit. For example, for IMO 9074729: (9×7) + (0×6) + (7×5) + (4×4) + (7×3) + (2×2) = 139. 139 % 10 = 9

"""