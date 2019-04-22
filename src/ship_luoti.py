
import datetime

import certifi
import urllib3
import pprint

import ship_info_extractors as sie


"""
Ship_luoti = Ship look up on the internet
Given an imo number. Try to look up the ship on a number of relevant web pages.
For each page compile a standard (dic) resume.
Return the list of dic's
"""

# Hardcoded constants
IMO = 7375765


def scan_marinetraffic_com(id, mode='imo'):
    """ Scan https://www.marinetraffic.com/en/ais/details/ships/imo:xxxxxxx
    Compile a dic report, and return it... """

    str_url = "https://www.marinetraffic.com/en/ais/details/ships/{}:{}".format(mode, id)
    print(str_url)
    user_agent = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    http = urllib3.PoolManager(10, headers=user_agent, cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET', str_url)
    dic_specs = dict()  # For collecting all specs about the ship
    dic_ship = sie.esi_marinetraffic_com(r.data, dic_specs)
    # Add meta data
    dic_ship['info_source'] = 'www.marinetraffic.com'
    dic_ship['info_update'] = datetime.datetime.now().isoformat()
    return dic_ship


def scan(imo, mode='imo'):
    lst_resi = list()
    # TBI: https://www.balticshipping.com/vessel/imo/8888630
    dic_resu = scan_marinetraffic_com(imo, 'imo')
    lst_resi.append(dic_resu)
    return lst_resi


def main(imo):
    lst_ret = list()  # Initialise list to return
    print("Scanning inet for: {}".format(imo))
    lst_resi = scan(imo, 'imo')
    return lst_resi

if __name__ == '__main__':

    imo = IMO  # Go with hardcoded default
    lst_res = main(imo)
    for dic_resu in lst_res:
        pprint.pprint(dic_resu)