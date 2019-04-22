
""" A number of semi-independent functions,
each designed to scrape ship info from a specific web site.
It would be nice if there were only one, but sites are uneven things ...

Each function should receive a 'bytes' data type, with the full html of a web page.
and a dictionary (maybe empty) to put data into, and return.
Each function returns the dictionary, with the relevant info added, semi-cleaned.

The 'bytes' input is designed to come from a http.request('GET', str_url).data request,
assuming http is a urllib3.PoolManager(). """

from bs4 import BeautifulSoup as bs
from bs4.element import Tag


# www.vesseltracker.com
def esi_vt(rdata, dic_ret=None):
    if dic_ret == None:
        dic_ret = dict()
    soup = bs(rdata, 'html.parser')
    # Ship name
    try:
        ship_name = soup.findAll('div', class_='page-title')[0].findAll('h1')[0].text
    except IndexError:
        ship_name = 'not found'
    #print(str(type(ship_name)), ship_name)
    if isinstance(ship_name, (str)) and len(ship_name) > 0:
        dic_ret['shipname'] = ship_name
    # The key-value tables
    lst_keyval = soup.findAll('div', 'key-value-table')
    for keyval in lst_keyval:
        for keya in keyval.contents:
            if "This information is available for registered users" in str(keya):
                continue
            #print("< {}".format(keya))
            keyr, valr = None, None
            for elem in keya.contents:
                #print("\t{}".format(elem))
                if " key" in str(elem):
                    keyr = elem.text
                elif " value" in str(elem):
                    valr = elem.text
                if keyr and valr:
                    dic_ret[keyr] = valr
                    #print("> {} > {}".format(keyr, valr))
    # Remove non-static info
    lst_bad_keys = ['Navigational status:', 'Course:', 'Heading:', 'Status:',
                    'Location:', 'Area:', 'Last seen:', 'From:',
                    'Last update:', 'Source:']
    for keyb in lst_bad_keys:
        try:
            del dic_ret[keyb]
        except KeyError:
            pass

    # Return
    return dic_ret


# www.marinetraffic.com
def esi_marinetraffic_com(byt_html, dic_specs):
    soup = bs(byt_html, 'html.parser')
    #print(soup.prettify())

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
                    dic_ret[kv[0].strip().rstrip(':').strip().lower()] = kv[
                        1].strip()
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
                    kv = [tok.strip() for tok in
                          span.get_text().strip().split(':')]
                    if len(kv) == 2:
                        dic_specs[kv[0].strip().rstrip(':').strip().lower()] = kv[1].strip()

    return dic_specs