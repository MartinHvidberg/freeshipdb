

import ship_show

IMO = '8917613'


def update_local_collect(imo=''):
    """ For the given IMO
    Walk all known _scrp tables
    transfer all (new) records to the collect table. """
    pass


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
    ship_show.main()