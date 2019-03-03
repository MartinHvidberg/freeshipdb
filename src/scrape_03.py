
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup as bs


def scrape_balticshipping_page(str_url, dic_ships):
    print("GET: {}".format(str_url))

    r = http.request('GET', str_url)
    soup = bs(r.data, 'html.parser')

    print("soup: {}\n\n".format(soup.prettify()))
    # # Harvest table
    # tabl = soup.findAll('table')#[0]
    # if tabl:
    #     print(tabl)
    # else:
    #     print("No table found on page: {}".format(str_url))

    return dic_ships


if __name__ == '__main__':

    str_url = "https://www.balticshipping.com/vessel/imo/9060730"

    user_agent = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}
    #http = urllib3.PoolManager(10, headers=user_agent)
    http = urllib3.PoolManager(10, headers=user_agent)
    # Scrape webpages to file
    while str_url:
        dic_bltic = scrape_balticshipping_page(str_url, dict())
        for keyi in dic_bltic.keys():
            print(keyi, dic_bltic[keyi])
        str_url = None
