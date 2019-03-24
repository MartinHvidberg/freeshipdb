-- Table: ais.ship_status

-- DROP TABLE ais.ship_status;

CREATE TABLE ais.ship_status
(
  ship_status_num integer,
  ship_status_txt character varying
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ais.ship_status
  OWNER TO g_geoint_a;
COMMENT ON TABLE ais.ship_status
  IS 'domain';


INSERT INTO ais.ship_status (ship_status_num, ship_status_txt) VALUES
    (0, 'Ordered'),
    (1, 'Delivered'),
    (2, 'Active'),
    (3, 'Active'),
    (4, 'Active'),
    (5, 'Active'),
    (6, 'Active'),
    (7, 'Missing'),
    (8, 'Sunk'),
    (9, 'Scrapped')
;