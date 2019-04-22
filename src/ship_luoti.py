
import certifi
import urllib3
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import pprint


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
    soup = bs(r.data, 'html.parser')
    #print(soup.prettify())

    dic_specs = dict()  # For collecting all specs about the ship

    # Get top-box and 'Position Received'
    
    def spans2dic(tag, dic_ret):
        for child in tag.children:
            if type(child) == Tag:
                kv = list()
                for grandchild in child.children:
                    if type(grandchild) == Tag:
                        gtt = grandchild.get_text()
                        kv.append(gtt)
                if len(kv) == 2:
                    dic_ret[kv[0].strip().rstrip(':').strip().lower()] = kv[1].strip()
        return dic_ret

    for span in soup.findAll('span'):  # Targetet to scrape Top-box and
        if 'AIS Vessel Type' in span.text:
            dic_specs = spans2dic(span.parent.parent, dic_specs)
        if 'Status:' in span.text:
            dic_specs = spans2dic(span.parent.parent, dic_specs)

    # Get 'General'

    for div in soup.findAll("div", {"id": "details_wiki_accordion"}):
        for hfour in div.findAll('h4'):
            if hfour.get_text() == 'General':
                for span in hfour.parent.parent.parent.findAll('span'):
                    kv = [tok.strip() for tok in span.get_text().strip().split(':')]
                    if len(kv) == 2:
                        dic_specs[kv[0].strip().rstrip(':').strip().lower()] = kv[1].strip()

    pprint.pprint(dic_specs)

def scan(imo, mode='imo'):
    lst_resi = list()
    # TBI: https://www.balticshipping.com/vessel/imo/8888630
    dic_resu = scan_marinetraffic_com(imo, 'imo')


def main(imo):
    lst_ret = list()  # Initialise list to return
    print("Scanning inet for: {}".format(imo))
    scan(imo, 'imo')
    return lst_ret

if __name__ == '__main__':

    imo = IMO  # Go with hardcoded default
    main(imo)