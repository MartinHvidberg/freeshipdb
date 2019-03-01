
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup as bs

str_url = r"www.shipnumber.com/"
http = urllib3.PoolManager()

def scrape_shipnumber(str_url, dic_ships):
    print("GET: {}".format(str_url))

    r = http.request('GET', str_url)
    soup = bs(r.data, 'html.parser')
    tabl = soup.findAll('table')[0]

    if tabl:
        num_row = 0
        for row in tabl.findAll('tr'):
            if num_row == 0:
                lst_header = [cel.text.strip() for cel in row.findAll('td')]
            else:
                lst_values = [cel.text.strip() for cel in row.findAll('td')]
                #print(lst_values)
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
    return "", dic_ships

dic_ships = dict()
while str_url:
    str_url, dic_ships = scrape_shipnumber(str_url, dic_ships)

with open("shipnumbers.csv", 'a') as filo:
    filo.write("IMO number,MMSI,Vessel Name,Call Sign,Vessel Type,flag,Gross Tonnage,Size,Year,update time" + '\n')
    for keys in dic_ships.keys():
        #print("ship: {} > {}".format(keys, dic_ships[keys]))
        str_ship = str()
        for keyt in ['IMO number','MMSI','Vessel Name','Call Sign','Vessel Type','flag','Gross Tonnage','Size','Year','update time']:
            #print(dic_ships[keys][keyt])
            str_ship = str_ship + dic_ships[keys][keyt] + ', '
        str_ship = str_ship.strip().strip(',')
        print("|{}|".format(str_ship))
        filo.write(str_ship+'\n')


#
# str_json = json.dumps(dic_ships, sort_keys=True, indent=4, separators=(',', ': '))
#
# with open("shipnumbers.json", "a") as filo:
#     filo.writelines(str_json)
