DELETE
FROM
    ais.shpnms_scrp a
        USING ais.shpnms_scrp b
WHERE
    a.ida < b.ida
    AND a.imo = b.imo
    AND a.mmsi = b.mmsi
    AND a.ship_name = b.ship_name
    AND a.callsign = b.callsign
    AND a.ship_type = b.ship_type
    AND a.flag = b.flag
    AND a.ship_weight_gt = b.ship_weight_gt
    AND a.ship_size_a = b.ship_size_a   
    AND a.ship_size_b = b.ship_size_b   
    AND a.xxx_year = b.xxx_year   
    AND a.xxx_update_time = b.xxx_update_time
;

DELETE
FROM
    ais.ship_collect a
        USING ais.ship_collect b
WHERE

    a.ida < b.ida
    AND a.imo = b.imo
    AND a.mmsi = b.mmsi
    AND a.ship_name = b.ship_name
    AND a.callsign = b.callsign
    AND a.ship_type = b.ship_type
    AND a.flag = b.flag
    AND a.ship_weight_gt = b.ship_weight_gt
    AND a.ship_size_a = b.ship_size_a   
    AND a.ship_size_b = b.ship_size_b   
    AND a.xxx_year = b.xxx_year   
    AND a.xxx_update_time = b.xxx_update_time

  AND a.imo = b.imo
  AND a.mmsi = b.mmsi
  AND a.callsign = b.callsign
  AND a.ship_name = b.ship_name
  AND a.ship_type = b.
  AND a.flag = b.
  AND a.ship_length = b.
  AND a.ship_width = b.
  AND a.ship_weight_gt = b.
  AND a.ship_weight_dw = b.
  AND a.ship_draught = b.
  AND a.ship_status = b.
  AND a.home_port = b.
  AND a.build_year = b.
  AND a.build_place = b.
  AND a.ship_owner = b.
  AND a.ship_operator = b.ship_operator
  AND a.classification_society = b.classification_society
  AND a.former_names = b.former_names
  AND a.info_source = b.info_source
  AND a.info_update = b.info_update
;