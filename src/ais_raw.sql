-- Table: ais.ais_raw

-- DROP TABLE ais.ais_raw;

CREATE TABLE ais.ais_raw
(
  ais_time character varying,
  ais_type character varying,
  mmsi bigint,
  lat real, -- d.d WGS84
  lon real, -- d.d WGS84
  navig_status character varying,
  rot real,
  sog real,
  cog real,
  heading smallint,
  imo character varying,
  callsign character varying,
  ship_name character varying,
  ship_type character varying,
  cargo_type character varying,
  ship_width real,
  ship_length real,
  posfix_type character varying,
  draught real,
  destination character varying,
  eta character varying,
  datasource character varying
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ais.ais_raw
  OWNER TO geoint_admin;
GRANT ALL ON TABLE ais.ais_raw TO geoint_admin;
GRANT ALL ON TABLE ais.ais_raw TO g_geoint_a WITH GRANT OPTION;
GRANT SELECT, UPDATE, INSERT, REFERENCES ON TABLE ais.ais_raw TO g_geoint WITH GRANT OPTION;
COMMENT ON COLUMN ais.ais_raw.lat IS 'd.d WGS84';
COMMENT ON COLUMN ais.ais_raw.lon IS 'd.d WGS84';


-- Index: ais.idx_raw_nav_stat

-- DROP INDEX ais.idx_raw_nav_stat;

CREATE INDEX idx_raw_nav_stat
  ON ais.ais_raw
  USING btree
  (navig_status COLLATE pg_catalog."default");
