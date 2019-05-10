-- Table: ais.dom_ship_status

-- DROP TABLE ais.dom_ship_status;

CREATE TABLE ais.dom_ship_status
(
  info_status_num integer,
  info_status_txt character varying
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ais.dom_ship_status
  OWNER TO g_geoint_a;
COMMENT ON TABLE ais.dom_ship_status
  IS 'domain';


INSERT INTO ais.dom_ship_status (info_status_num, info_status_txt) VALUES
    (0, 'Unknown'),  -- We have no information
    (1, 'Undefined'),  -- We have info, but it do not match any of the allowed values
    (2, 'Ordered'),  -- Shipyard is building it
    (3, 'Delivered'),  -- Not yet in service
    (4, 'Active'),  -- In service
    (5, 'inactive, but operative'),  -- Hotelship, etc
    (6, 'Missing'),  -- Whereabouts unknown
    (7, 'Damaged, inoperative'),  -- Firedamaged, etc
    (8, 'Sunk, inoperative'),
    (9, 'Scrapped')
;
