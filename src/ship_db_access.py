
import sys

import psycopg2

import ecpw  # The EC-password module (local copy)

DEBUG = False

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
        str_dsn = con.get_dsn_parameters()  # PostgreSQL Connection properties
        cur.execute("SELECT version();")  # PostgreSQL version
        str_ver = cur.fetchone()
        if DEBUG:
            print("WHOAMI {}:\n  Conn.: {}\n   Ver.: {}".format(__file__, str_dsn, str_ver))
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    sys.exit(999)


def get_raw_rows_from_table(key, val, table, schema='ais'):
    """ Get the relevant row(s) from a table """
    str_sql = "SELECT * FROM {}.{} WHERE {} = {};".format(schema, table, key, val)
    with con.cursor() as cur:
        cur.execute(str_sql)
        lst_val = cur.fetchall()
    return lst_val


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
    """ Get the relevant row(s) from a table """
    lst_val = get_raw_rows_from_table(key, val, table, schema)
    ##print("raw sql res N={}: {}".format(len(lst_val), lst_val))
    lst_ret = list()
    for raw in lst_val:
        dic_ret = dict()
        for n in range(len(lst_fld)):
            fldn = lst_fld[n]
            valn = raw[n]
            dic_ret[fldn] = valn
        lst_ret.append(dic_ret)
    return lst_ret


def delete_data_from_table(key, val, table, schema='ais'):
    """ REMOVE the relevant rows from the table """
    str_sql = "DELETE FROM {}.{} WHERE {} = {};".format(schema, table, key, val)
    with con.cursor() as cur:
        cur.execute(str_sql)
    con.commit()

def insert_dic_in_coll(dic_cand):
    """
    Inserts the new candidates (that have been checked elsewhere)
    into 'collection'
    example:
    INSERT INTO ais.ship_collect(
            imo, mmsi, callsign, ship_name, ship_type, flag,
            ship_length, ship_width, ship_weight_gt, ship_weight_dw, ship_draught,
            ship_status, home_port, build_year, build_place, ship_owner, ship_operator,
            classification_society, former_names, info_source, info_update)
    VALUES (8917613, 219592000, 'OXRA6', 'CROWN SEAWAYS', 'Passenger ship', 'Denmark',
            171.0, 28.0, 0, 0, 0.0,
            '', '', 0, '', '', '',
            '', '', 'vesseltracker.com', '2018-03-24');"""
    lst_k, lst_v = [], []
    for k in dic_cand.keys():
        if k in LST_FLD:
            lst_k.append(k)
            obj_val = dic_cand[k]
            if isinstance(obj_val, str) and "'" in obj_val:
                obj_val = obj_val.replace("'", "")
            lst_v.append(obj_val)
    str_k = str(lst_k).replace("'","").replace("[","").replace("]","")
    str_v = str(lst_v).replace('None',"Null").replace("[","").replace("]","")
    str_sql = "INSERT INTO ais.ship_collect({}) VALUES ({});".format(str_k, str_v)
    with con.cursor() as cur:
        ##print("SQL: {}".format(str_sql))
        cur.execute(str_sql)
    con.commit()
