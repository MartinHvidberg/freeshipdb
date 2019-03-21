
lst_case = [1,1,2,3, 3, 4]

def lod_remove_duplicates(lst_in):
    lst_ret = list()
    for itmi in lst_in:
        bol_new = True  # Assumed new, until proven redundant
        for itmo in lst_ret:
            if itmo == itmi:
                bol_new = False
                continue
        if bol_new:
            lst_ret.append(itmi)
    return lst_ret

print(lod_remove_duplicates(lst_case))