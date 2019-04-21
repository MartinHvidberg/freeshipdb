

import datetime

import ship_luis  # Look Up In Scrapes, fill in _collected
import ship_luoti  # Look Up On The Internet, fill in _collected
import ship_ulmui  # Update Local Most Updated Info, from _collected
import ship_show

#import ship_db_access as db
#import ship_ec_helpers as ec


# Hardcoded constants
IMO = '5351894' # ''8917613' # '8888630' #
LST_FLD = ['imo', 'mmsi', 'callsign', 'ship_name', 'ship_type', 'flag',
           'ship_length', 'ship_width',
           'ship_weight_gt', 'ship_weight_dw', 'ship_draught',
           'ship_status', 'home_port', 'build_year', 'build_place',
           'ship_owner', 'ship_operator', 'classification_society',
           'former_names', 'info_source', 'info_update']


def main(imo):

    # 1 LUIS: Look Up In Scrapes, fill in _collected
    dtt_start = datetime.datetime.now()
    ship_luis.ship_luis(imo)  # Look Up In Scrapes, i.e. Collect data from all available scrp tables
    print("... Ship Look up in Scrapes: {:.3} ms".format((datetime.datetime.now() - dtt_start).total_seconds()*1000))

    # 2 LUOTI: Look Up On The Internet, fill in _collected. This makes more sence with imo, as it's the more widely searchable identifyer
    dtt_start = datetime.datetime.now()
    lst_soti = ship_luoti.main(imo)
    print("... Ship Look up on the internet: {:.3} ms".format((datetime.datetime.now() - dtt_start).total_seconds()*1000))

    # 3 ULMUI: Update Local Most Updated Info, from _collected. This makes more sence with mmsi, as it's a more specific identifyer
    dtt_start = datetime.datetime.now()
    ship_ulmui.update_local_mui(mmsi)  # Update Most Updated Info, based on all collected info
    print("... Present up-to-date ship data: {:.3} ms".format((datetime.datetime.now() - dtt_start).total_seconds()*1000))

    # 4 SHOW: Present up-to-date ship data
    dtt_start = datetime.datetime.now()
    ship_show.imo(imo)
    print("... Present up-to-date ship data: {:.3} ms".format((datetime.datetime.now() - dtt_start).total_seconds()*1000))

if __name__ == '__main__':

    main(IMO)