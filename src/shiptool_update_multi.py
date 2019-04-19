import sys

import psycopg2

import ship_update
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
        print("WHOAMI {}:\n  {}".format(__file__, con.get_dsn_parameters()))
        # Print PostgreSQL version
        cur.execute("SELECT version();")
        record = cur.fetchone()
        print("  Conn..:", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    sys.exit(999)


if __name__ == "__main__":

    str_sql = "SELECT DISTINCT {} FROM {}.{};".format('imo', 'ais', 'shpnms_scrp')
    with con.cursor() as cur:
        cur.execute(str_sql)
        rows = cur.fetchall()
        for row in rows:
            imonr = row[0]
            print("Multi: handle: {}".format(imonr))
            if __name__ == '__main__':
                ship_update.main(imonr)
