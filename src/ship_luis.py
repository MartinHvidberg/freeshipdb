
import ship_db_access as db
import ship_ec_helpers as ec

KNOWN_SCRP_TABLES = ['vestra_scrp', 'shpnms_scrp']


def check_swap_length_width(dic_in):
    """ Check if ship is wider then long, then swap meassures """
    if all ([para in dic_in.keys() for para in ['ship_length', 'ship_width']]):
        if dic_in['ship_width'] > dic_in['ship_length']:  # if it's wider than long
            dic_in['ship_width'], dic_in['ship_length'] = dic_in['ship_length'], dic_in['ship_width']
    return dic_in


def homogene_names(lst_in, source_id):
    """ Take a dic, based on the local names from a scrape source,
    and convert them to common collection names"""

    def substitute(dic_in, str_a, str_b):
        if str_a in dic_in.keys():
            dic_in[str_b] = dic_in[str_a]
            del dic_in[str_a]
        return dic_in

    lst_ret = list()
    for dic_in in lst_in:
        if source_id == 'vestra_scrp':  # Vessel Tracker
            # Expect: ['shipname', 'mmsi', 'imo', 'imovalid', 'callsign', 'aistype', 'shiplength', 'shipwidth', 'flag']
            dic_in = substitute(dic_in, 'aistype', 'ship_type')
            dic_in = substitute(dic_in, 'shiplength', 'ship_length')
            dic_in = substitute(dic_in, 'shipwidth', 'ship_width')
            dic_in['info_source'] = 'vesseltracker.com'
        elif source_id == 'shpnms_scrp':  # Ship Names
            # Expect: ['ida', 'imo', 'mmsi', 'ship_name', 'callsign', 'ship_type', 'flag', 'ship_weight_gt', 'ship_size_a', 'ship_size_b', 'xxx_year', 'xxx_update_time']
            dic_in = substitute(dic_in, 'ship_size_a', 'ship_length')
            dic_in = substitute(dic_in, 'ship_size_b', 'ship_width')
            dic_in = check_swap_length_width(dic_in)
            dic_in = substitute(dic_in, 'xxx_year', 'build_year')
            dic_in = substitute(dic_in, 'xxx_update_time', 'info_update')
            dic_in['info_source'] = 'shipnumber.com'
        lst_ret.append(dic_in)

    return lst_ret


def ship_luis(imo):
    """ Look Up In Scrapes, i.e. For the given imo
    Walk all known _scrp tables
    transfer all (new) records to the collect table. """
    print("Scanning local db for: {}".format(imo))

    # get the _scrp data, include DELETE them from input table
    lst_all_scrps = list()
    for scrp_source in KNOWN_SCRP_TABLES:
        lst_flds_source = db.get_fieldnames_from_table(scrp_source)
        lst_scrp = db.get_data_from_table('imo', imo, scrp_source, lst_flds_source)
        if len(lst_scrp) > 0:
            # The DELETE part
            db.delete_data_from_table('imo', imo, scrp_source)
        lst_scrp = homogene_names(lst_scrp, scrp_source)
        ##print("scpret {} {} {}".format(scrp_source, len(lst_scrp), lst_scrp))
        lst_all_scrps.extend(lst_scrp)  # add to the main list
        del lst_flds_source, lst_scrp  # clean before looping ...
    lst_all_scrps = ec.lod_remove_duplicates(lst_all_scrps)  # Remove duplicates
    ##print("scpret ALL         {}".format(len(lst_all_scrps)))

    # get existing collect data
    lst_flds_source = db.get_fieldnames_from_table('ship_collect')
    lst_coll = db.get_data_from_table('imo', imo, 'ship_collect', lst_flds_source)
    ##print("colret {} {} {}".format(scrp_source, len(lst_coll), lst_coll))

    # Evaluate scrapes for potential adding to collect
    for dic_cand in lst_all_scrps:
        if not any ([ec.redundant_dic(dic_cand, dic_coll) for dic_coll in lst_coll]):
            db.insert_dic_in_coll(dic_cand)


