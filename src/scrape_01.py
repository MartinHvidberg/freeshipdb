
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

with open("sites.csv", "r") as fils:
    lst_sites = fils.readlines()
site1 = [tok.strip().replace('"','') for tok in lst_sites[0].split(',')]
print(site1)
mmsi = 7116808
str_url = "{}{}{}{}".format(site1[0], site1[1], str(mmsi), site1[2])
print(str_url)


http = urllib3.PoolManager()
r = http.request('GET', str_url)
print(r.status)
#200
soup = BeautifulSoup(r.data, 'html.parser')

mydivs = soup.findAll("div", {"class": "row"})
keyval = soup.find("div", "key-value-table")
print(str(type(keyval)), keyval)
for desn in keyval.descendants:
    print('\n', desn)
#imo = keyval.findnext('div', "key")
#print(imo)

with open('7116808.html', 'w') as filo:
    filo.write(str(soup))
