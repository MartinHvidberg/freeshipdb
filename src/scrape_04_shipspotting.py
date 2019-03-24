
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup as bs


def scrape_shipspot_imagepage(str_url, dic_ship):
    """ From a 'image' page on shipspotting.com
    scrape the ship specific info.
    append it to the dic_ship,
    return the dic_ship"""
    print("GET more: {}".format(str_url))
    r = http.request('GET', str_url)
    soup = bs(r.data, 'html.parser')
    ##print("soup: {}".format(soup.prettify()))
    # suck table with 'Vessel type'
    lst_hit = soup.findAll("td", text="Vessel type:")
    if lst_hit:
        for row in lst_hit[0].parent.parent:
            k,v = row.text.split(':', 1)
            dic_ship[k] = v
    # suck table with 'Class society'
    lst_hit = soup.findAll("td", text="Class society:")
    if lst_hit:
        for row in lst_hit[0].parent.parent:
            #print("Nice row: {}".format(row.prettify()))
            k,v = row.text.split(':', 1)
            dic_ship[k] = v
    return dic_ship

def scrape_shipspot_page(str_url, dic_ships):
    """ From a 'general' info page on shipspotting.com
    scrape the general info, and look for image that can lead to detailed info.
    Create and fill a dic_ship,
    and append it to dic_ships   XXX Change that XXX
    return dic_ships"""

    print("GET base: {}".format(str_url))
    try:
        num_imo = int(str_url.rsplit("=", 1)[1])
    except ValueError:
        print("Can't find IMO in: {}".format(str_url))
        return dic_ships

    r = http.request('GET', str_url)
    soup = bs(r.data, 'html.parser')

    # Harvest table 'General Information'
    lst_tbls = soup.findAll('table', {'width':'100%'})
    lst_tbls = [tbl for tbl in lst_tbls if 'IMO:' in tbl.text]
    lst_tbls = [tbl for tbl in lst_tbls if 'MMSI:' in tbl.text]
    #lst_tbls = [tbl for tbl in lst_tbls if 'Callsign:' in tbl.text]
    #lst_tbls = [tbl for tbl in lst_tbls if 'Vessel type:' in tbl.text]
    #lst_tbls = [tbl for tbl in lst_tbls if 'Current flag:' in tbl.text]
    if lst_tbls:
        if len(lst_tbls) == 1:
            tbl = lst_tbls[0]
            for tr in tbl.findAll('tr'):
                for td in tr.findAll('td'):
                    lst_spoof = td.prettify()\
                        .replace('\n', ' ')\
                        .replace('<br/>', '\n')\
                        .replace('</div>', '\n')\
                        .replace('<b>', '')\
                        .replace('</b>', '')\
                        .strip().split('\n')
                    dic_ship = dict()
                    for tok in lst_spoof:
                        #print("   {}".format(tok))
                        if len(tok.split(':')) == 2:
                            keys, vals = [kv.strip() for kv in tok.split(':')]
                            #print("kv: {}::{}".format(keys, vals))
                            if keys in ['Current name','IMO','Callsign','MMSI',
                                        'Vessel type','Build year',
                                        'Current flag','Home port']:
                                dic_ship[keys] = vals
        else:
            print("Did not find exactely 1 table. Found: {}".format(len(lst_tbls)))
    else:
        print("No table found on page: {}".format(str_url))

    # Look for image, and hunt more info
    lst_anchs = [anch for anch in soup.findAll('a') if 'gallery/photo.php' in anch.get('href')]
    if lst_anchs and len(lst_anchs) > 0:
        dic_ship = scrape_shipspot_imagepage(lst_anchs[0].get('href'), dic_ship)


    # Show
    for itm in dic_ship.keys():
        print("ship[imo{}] {} : {}".format(num_imo, itm, dic_ship[itm]))

    dic_ships[str(num_imo)] = dic_ship

    return dic_ships


if __name__ == '__main__':

    str_url = "http://www.shipspotting.com/ships/ship.php?imo=9681895" # 9241267 # 5383304

    user_agent = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    http = urllib3.PoolManager(10, headers=user_agent)
    # Scrape webpages to file
    while str_url:
        dic_shipspot = scrape_shipspot_page(str_url, dict())
        # for keyi in dic_shipspot.keys():
        #     print("KV: {} {}".format(keyi, dic_shipspot[keyi]))
        str_url = None
