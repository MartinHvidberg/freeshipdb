def redundant_dic(dic_cand, dic_reff):
    """ If dic_cand hold informations not represented in dic_reff,
    then return False, else return True
    :param dic_cand: dictionary
    :param dic_reff: dictionaty
    :return: True | False
    """
    for key_c in dic_cand.keys():
        if not key_c in dic_reff.keys():
            return False
        else:
            if dic_cand[key_c] != dic_reff[key_c]:
                return False
    return True

def lod_remove_duplicates(lst_in):
    lst_ret = list()
    for itmi in lst_in:
        bol_new = True  # Assumed new, until proven redundant
        for itmo in lst_ret:
            if redundant_dic(itmo, itmi):
                bol_new = False
                continue
        if bol_new:
            lst_ret.append(itmi)
    return lst_ret


