from bs4 import BeautifulSoup as bs

def esi_vt(rdata):
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
