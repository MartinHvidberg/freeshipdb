import os
import sys

import psycopg2

try:
    connection = psycopg2.connect(user="mh",
                                  password="***",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="snaps")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print("WHOAMI: {}".format(connection.get_dsn_parameters()))
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    sys.exit(999)

root_dir = r"../data/eci/7/"

cnt = 0
lst_k = list()
for r, d, f in os.walk(root_dir):
    for fil in f:
        if ".eci" in fil:
            str_ffn =os.path.join(r, fil)
            # Read the data
            with open(str_ffn, 'r') as fil_eci:
                dat_eci = fil_eci.readlines()
                if len(dat_eci) == 1:
                    lst_eci = [tok.strip() for tok in dat_eci[0].strip('{}').split(',')]
                    dic_eci = dict()
                    for tok in lst_eci:
                        lst_par = [kv.strip() for kv in tok.rsplit(':', 1)]
                        if len(lst_par) == 2:
                            k = lst_par[0].replace("'", "").replace(":", "").strip().lower()
                            v = lst_par[1].strip().strip("'").strip()
                            # Cleaning
                            if k not in ['shipname', 'mmsi', 'imo', 'imovalid',
                                         'callsign', 'ais type', 'length',
                                         'width', 'flag']:
                                continue
                            v = v.replace("'", "").replace('"', '')
                            if k == 'length' or k == 'width':
                                for c in set(v):
                                    if c not in "0123456789.,":
                                        v = v.replace(c, '')
                                if v == '': v = '0'
                            if k == 'imo' and 'invalid' in v:
                                v = v.replace('invalid', '')
                                dic_eci['imovalid'] = 0
                            else:
                                dic_eci['imovalid'] = 1
                            # Insert
                            dic_eci[k] = v
                            lst_k.append(k)
                            lst_k = list(set(lst_k))
                        else:
                            print("Pair is not length 2: {} in {}".format(tok, str_ffn))
                    if isinstance(lst_eci, list):
                        pass
                    else:
                        print(".eci file can't be converted to dic: {}".format(dat_eci))
                else:
                    print("Unexpected != 1 lines in .eci: {} > {}".format(str_ffn, dat_eci))
            # Write the data to PostgreSQL
            #print(dic_eci)
            if 'imo' in dic_eci and len(dic_eci['imo']) > 0:
                lst_keys, lst_vals = [], []
                for keyk in dic_eci.keys():
                    lst_keys.append(keyk)
                    lst_vals.append(dic_eci[keyk])
                str_keys = str(lst_keys).strip("[]").replace("'", '"').lower()
                str_keys = str_keys.replace("ais type", "aistype")
                str_keys = str_keys.replace("length", "shiplength")
                str_keys = str_keys.replace("width", "shipwidth")
                str_vals = str(lst_vals).strip("[]")
                sql = "INSERT INTO ais.scrp_vestra({}) VALUES({});".format(str_keys, str_vals)
                print("SQL: {}".format(sql))
                cursor.execute(sql)
                connection.commit()

                cnt += 1

print("processed .eci files: {}".format(cnt))

# closing database connection.
if (connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
