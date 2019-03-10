
fnfpi = r"/home/martin/PycharmProjects/freeshipdb/data/shpnms/shipnumbers_allcln.csv"
fnfpo = r"/home/martin/PycharmProjects/freeshipdb/data/shpnms/shipnumbers_allcl2.csv"


def small_check(str_in):
    if ',' in str_in:
        if len(str_in) > 7:
            if len(str_in.split(',')) == 11:
                return 1
            else:
                return 0


def fix_small(str_in):
    str_ret = str_in  # In case of no changes, return original data
    # usual suspects

    lst_in = str_ret.strip().split(',')
    if 'x' in lst_in[7]:  # ship_size_a and ship_size_b not split
        lst_new7 = [tok.replace('m', '').strip() for tok in lst_in[7].split('x')]
        lst_new = lst_in[:7] + lst_new7 + lst_in[8:]
        str_ret = str(lst_new)\
                      .replace("'", "")\
                      .replace(' ,',',')\
                      .replace(', ',',')\
                      .strip('[]')\
                      .strip()\
                      +'\n'

    lst_in = str_ret.strip().split(',')
    if 'N/A' in lst_in[7] or lst_in[7] == '':  # ship_size is undefined
        lst_new7 = [0, 0]
        lst_new = lst_in[:7] + lst_new7 + lst_in[8:]
        str_ret = str(lst_new)\
                      .replace("'", "")\
                      .replace(' ,',',')\
                      .replace(', ',',')\
                      .strip('[]')\
                      .strip()\
                      +'\n'

    lst_in = str_ret.strip().split(',')
    if 'y' in lst_in[9].lower():  # still 'Y' in Year
        #print("Bonus: {}".format(lst_in[9]))
        lst_new = lst_in
        lst_new[9] = lst_in[9].lower().replace('y', '')
        str_ret = str(lst_new)\
                      .replace("'", "")\
                      .replace(' ,',',')\
                      .replace(', ',',')\
                      .strip('[]')\
                      .strip()\
                      +'\n'
    print("Replacestring...: {}".format(str_ret))
    return str_ret

def big_check(str_in):
    pass

with open(fnfpo, 'w') as filo:
    with open(fnfpi, 'r') as fili:
        cnt = 0
        okay = 0
        for line in fili:
            chks = small_check(line)
            if chks == 0:
                line = fix_small(line)
                chks = small_check(line)  # Second chance to be good
                if chks == 0:  # Still error?
                    print("Err2: {}".format(line))
            okay += chks
            #big_check(line)
            filo.write(line)
            cnt += 1
print(cnt, okay)