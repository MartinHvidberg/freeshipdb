
import sys

import ship_db_access as db


def imo(imo):
        print('Showing info for IMO: {}'.format(imo))
        table = "ship_collect"
        # str_sql = "select * from ais.{} where imo = {};".format(table, imo)
        # # print('\n', str_sql)
        # with con.cursor() as cur:
        #     cur.execute(str_sql)
        #     lst_hit = cur.fetchall()
        lst_hit = db.get_raw_rows_from_table('imo', imo, table)
        for hit in lst_hit:
            print("scol: {}".format(hit))
        lst_ret = [tok[0] for tok in lst_hit]
        return lst_ret


def mmsi(mmsi):
        print('Showing info for MMSI: {}'.format(mmsi))


if __name__ == '__main__':

    if sys.argv and len(sys.argv) > 1:
        imo(sys.argv[1])
        mmsi(sys.argv[1])
    else:
        print('Please indicate IMO number')