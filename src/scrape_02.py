
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup as bs

URL_START = r"http://www.shipnumber.com/"
LST_KEYT = ['IMO number', 'MMSI', 'Vessel Name', 'Call Sign', 'Vessel Type',
            'flag', 'Gross Tonnage', 'Size', 'Year', 'update time']
HEADER = "IMO number,MMSI,Vessel Name,Call Sign,Vessel Type," \
         "flag,Gross Tonnage,Size,Year,update time"
STR_FILO = "shipnumbers.csv"

def scrape_shipnumber_page(str_url, dic_ships):
    print("GET: {}".format(str_url))

    r = http.request('GET', str_url)
    soup = bs(r.data, 'html.parser')

    # Harvest table
    tabl = soup.findAll('table')[0]
    if tabl:
        num_row = 0
        for row in tabl.findAll('tr'):
            if num_row == 0:
                lst_header = [cel.text.replace(',',';').strip() for cel in row.findAll('td')]
            else:
                lst_values = [cel.text.replace(',',';').strip() for cel in row.findAll('td')]
                dic_tmp = dict()
                for n in range(len(lst_header)):
                    dic_tmp[lst_header[n]] = lst_values[n]
                if "IMO number" in dic_tmp.keys():
                    dic_ships[dic_tmp["IMO number"]] = dic_tmp
                else:
                    print("No IMO-number entry in dic: {}".format(dic_tmp))
            num_row += 1
    else:
        print("No table found on page: {}".format())

    # Harves Next
    try:
        str_a_next = [tok for tok in soup.findAll('a') if tok.text == 'next'][0]
        str_next = str_url.rsplit('/', 1)[0] + '/' + str_a_next.get('href')
    except IndexError as e:
        print("Seems we have reached the last page - no more 'next")
        str_next = None

    return str_next, dic_ships

if __name__ == '__main__':

    str_url = URL_START
    http = urllib3.PoolManager()
    # Open out file and write header
    with open(STR_FILO, 'w') as filo:
        filo.write(HEADER+'\n')
    # Scrape webpages to file
    while str_url:
        str_url, dic_ships = scrape_shipnumber_page(str_url, dict())
        with open(STR_FILO, 'a') as filo:
            for keys in dic_ships.keys():
                str_ship = str()
                for keyt in LST_KEYT:
                    str_ship = str_ship + dic_ships[keys][keyt] + ', '
                str_ship = str_ship.strip().strip(',')
                #print("|{}|".format(str_ship))
                filo.write(str_ship+'\n')


#
# str_json = json.dumps(dic_ships, sort_keys=True, indent=4, separators=(',', ': '))
#
# with open("shipnumbers.json", "a") as filo:
#     filo.writelines(str_json)
