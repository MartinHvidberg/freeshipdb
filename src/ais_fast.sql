-- Table: ais.ais_fast

-- DROP TABLE ais.ais_fast;

CREATE TABLE ais.ais_fast
(
  ida bigserial NOT NULL,
  ais_timestmp timestamp without time zone NOT NULL,
  ais_type smallint, -- 1 "Class A", 2 "Class B"
  mmsi bigint NOT NULL,
  lat real NOT NULL, -- d.d WGS84
  lon real NOT NULL, -- d.d WGS84
  navig_status smallint, -- 0..15
  rot real,
  sog real,
  cog real,
  heading smallint,
  posfix_type smallint,
  draught real,
  destination character varying,
  CONSTRAINT ais_fast_pkey PRIMARY KEY (ida)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ais.ais_fast
  OWNER TO geoint_admin;
GRANT ALL ON TABLE ais.ais_fast TO geoint_admin;
GRANT ALL ON TABLE ais.ais_fast TO g_geoint_a WITH GRANT OPTION;
GRANT SELECT, UPDATE, INSERT, REFERENCES ON TABLE ais.ais_fast TO g_geoint WITH GRANT OPTION;
COMMENT ON COLUMN ais.ais_fast.ais_type IS '1 "Class A", 2 "Class B"';
COMMENT ON COLUMN ais.ais_fast.lat IS 'd.d WGS84';
COMMENT ON COLUMN ais.ais_fast.lon IS 'd.d WGS84';
COMMENT ON COLUMN ais.ais_fast.navig_status IS '0..15';


-- Index: ais.idx_fast_ais_type

-- DROP INDEX ais.idx_fast_ais_type;

CREATE INDEX idx_fast_ais_type
  ON ais.ais_fast
  USING btree
  (ais_type);

-- Index: ais.idx_fast_lat

-- DROP INDEX ais.idx_fast_lat;

CREATE INDEX idx_fast_lat
  ON ais.ais_fast
  USING btree
  (lat);

-- Index: ais.idx_fast_lon

-- DROP INDEX ais.idx_fast_lon;

CREATE INDEX idx_fast_lon
  ON ais.ais_fast
  USING btree
  (lon);

-- Index: ais.idx_fast_mmsi

-- DROP INDEX ais.idx_fast_mmsi;

CREATE INDEX idx_fast_mmsi
  ON ais.ais_fast
  USING btree
  (mmsi);

-- Index: ais.idx_fast_nav_stat

-- DROP INDEX ais.idx_fast_nav_stat;

CREATE INDEX idx_fast_nav_stat
  ON ais.ais_fast
  USING btree
  (navig_status);

-- Index: ais.idx_fast_timestamp

-- DROP INDEX ais.idx_fast_timestamp;

CREATE INDEX idx_fast_timestamp
  ON ais.ais_fast
  USING btree
  (ais_timestmp);

