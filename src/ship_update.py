
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


def get_fieldnames_from_table(table, schema='ais'):
    # * get the field names
    str_sql = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name ='{}';".format(table)
    #print('\n', str_sql)
    with con.cursor() as cur:
        cur.execute(str_sql)
        lst_fld = cur.fetchall()
    lst_ret = [tok[0] for tok in lst_fld]
    print("fldret", lst_ret)
    return lst_ret


def get_data_from_table(key, val, table, lst_fld, schema='ais'):
    str_sql = "SELECT * FROM {}.{} WHERE {} = {};".format(schema, table, key, val)
    with con.cursor() as cur:
        cur.execute(str_sql)
        lst_val = cur.fetchall()
    print(lst_val)
    dic_ret = dict()
    for n in range(len(lst_fld)):
        fldn = lst_fld[n][0]
        valn = lst_val[0][n]
        dic_ret[fldn] = valn
    return dic_ret


def update_local_collect(imo=''):
    """ For the given IMO
    Walk all known _scrp tables
    transfer all (new) records to the collect table. """
    # get the _scrp data
    lst_flds_vestra = get_fieldnames_from_table('vestra_scrp')
    lst_vstra = get_data_from_table('imo', imo, 'vestra_scrp', lst_flds_vestra)
    print(str(type(lst_vstra)), len(lst_vstra), lst_vstra)
    lst_flds_shpnms = get_fieldnames_from_table('shpnms_scrp')
    lst_shpnm = get_data_from_table('imo', imo, 'shpnms_scrp', lst_flds_shpnms)
    print(str(type(lst_shpnm)), len(lst_shpnm), lst_shpnm)
    # get existing collect data
    lst_colle = 0

def update_local_mui(imo=''):
    """ For the given IMO
    Consider all relevant records in collect table
    (re)write most updated info to _mui table"""
    pass

if __name__ == '__main__':

    # 1 Look ship up in local data
    update_local_collect(IMO)  # Collect data from all available scrp tables
    update_local_mui(IMO)  # Update Most Updated Info, based on all collected info

    # 2 Look ship up on the internet


    # 3 Compare, and maybe update, local data


    # 4 show up-to-date ship data
    ship_show.main(IMO)