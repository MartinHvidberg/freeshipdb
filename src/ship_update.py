
import sys

import psycopg2

import ship_show
import ecpw  # The EC-password module (local copy)

# Establist connection to DB
ecs = ecpw.Store()
db_ip, db_port, db_database, db_name, db_pw = ecs.gets('PostgreSQL_mh', ['ip', 'port' , 'database', 'name', 'password'])
try:
    con = psycopg2.connect(user=db_name,
                           password=db_pw,
                           host=db_ip,
                           port=db_port,
                           database=db_database)
    with con.cursor() as cur:
        # Print PostgreSQL Connection properties
        print("WHOAMI: {}".format(con.get_dsn_parameters()))
        # Print PostgreSQL version
        cur.execute("SELECT version();")
        record = cur.fetchone()
        print("Conn..:", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    sys.exit(999)


# Hardcoded constants
IMO = '8917613'
LST_FLD = ['imo', 'mmsi', 'callsign', 'ship_name', 'ship_type', 'flag',
           'ship_length', 'ship_width',
           'ship_weight_gt', 'ship_weight_dw', 'ship_draught',
           'ship_status', 'home_port', 'build_year', 'build_place',
           'ship_owner', 'ship_operator', 'classification_society',
           'former_names', 'info_source', 'info_update']


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

def get_fieldnames_from_table(table, schema='ais'):
    # * get the field names
    str_sql = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name ='{}';".format(table)
    #print('\n', str_sql)
    with con.cursor() as cur:
        cur.execute(str_sql)
        lst_fld = cur.fetchall()
    lst_ret = [tok[0] for tok in lst_fld]
    return lst_ret


def get_data_from_table(key, val, table, lst_fld, schema='ais'):
    """ Get the relevant row(s) from a table, and then REMOVE them from the table """
    str_sql = "SELECT * FROM {}.{} WHERE {} = {};".format(schema, table, key, val)
    with con.cursor() as cur:
        cur.execute(str_sql)
        lst_val = cur.fetchall()
    ##print("raw sql res N={}: {}".format(len(lst_val), lst_val))
    lst_ret = list()
    for raw in lst_val:
        dic_ret = dict()
        for n in range(len(lst_fld)):
            fldn = lst_fld[n]
            valn = raw[n]
            dic_ret[fldn] = valn
        lst_ret.append(dic_ret)

    # The REMOVE part
    # TBI
    return lst_ret


def insert_dic_in_coll(dic_cand):
    """
    Inserts the new candidates (that have been checked elsewhere)
    into 'collection' """
    pass


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


def update_local_collect(imo):
    """ For the given IMO
    Walk all known _scrp tables
    transfer all (new) records to the collect table. """
    # get the _scrp data
    lst_all_scrps = list()
    for scrp_source in ['vestra_scrp', 'shpnms_scrp']:
        lst_flds_source = get_fieldnames_from_table(scrp_source)
        #print("fldret {} : {}".format(scrp_source, lst_flds_source))
        lst_scrp = get_data_from_table('imo', imo, scrp_source, lst_flds_source)
        lst_scrp = homogene_names(lst_scrp, scrp_source)
        print("scpret {} {} {}".format(scrp_source, len(lst_scrp), lst_scrp))
        lst_all_scrps.extend(lst_scrp)  # add to the main list
        del lst_flds_source, lst_scrp  # clean before looping ...
    lst_all_scrps = lod_remove_duplicates(lst_all_scrps)  # Remove duplicates
    ##print("scpret ALL         {} {}".format(len(lst_all_scrps), lst_all_scrps))
    print("scpret ALL         {}".format(len(lst_all_scrps)))

    # get existing collect data
    lst_flds_source = get_fieldnames_from_table('ship_collect')
    lst_coll = get_data_from_table('imo', imo, 'ship_collect', lst_flds_source)
    print("colret {} {} {}".format(scrp_source, len(lst_coll), lst_coll))

    # Evaluate scrapes for potential adding to collect
    for dic_cand in lst_all_scrps:
        if not any ([redundant_dic(dic_cand, dic_coll) for dic_coll in lst_coll]):
            insert_dic_in_coll(dic_cand)


    ##lst_colle = 0

def update_local_mui(imo=''):
    """ For the given IMO
    Consider all relevant records in collect table
    (re)write most updated info to _mui table"""
    pass

if __name__ == '__main__':

    # 1 Look ship up in local data
    update_local_collect(IMO)  # Collect data from all available scrp tables

    # 2 Look ship up on the internet


    # 3 Compare, and maybe update, local data


    # 4 Present up-to-date ship data
    update_local_mui(IMO)  # Update Most Updated Info, based on all collected info
    ship_show.main(IMO)