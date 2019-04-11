
--
-- Pre Process...
--

-- Role: g_geoint

-- DROP ROLE g_geoint;

CREATE ROLE g_geoint
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

-- Role: g_geoint_a

-- DROP ROLE g_geoint_a;

CREATE ROLE g_geoint_a
  SUPERUSER INHERIT CREATEDB CREATEROLE NOREPLICATION;
GRANT g_geoint TO g_geoint_a;

-- Role: geoint_admin

-- DROP ROLE geoint_admin;

CREATE ROLE geoint_admin LOGIN
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT g_geoint TO geoint_admin;
GRANT g_geoint_a TO geoint_admin;
COMMENT ON ROLE geoint_admin IS 'Admin user for the GEOINT database(s)
sgnnnn, where nn is persillehakkerkode';

-- Role: mh

-- DROP ROLE mh;

CREATE ROLE mh LOGIN
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT g_geoint TO mh;
COMMENT ON ROLE mh IS 'Non-super Bondemand pasword: bareskiftdet';

-- Database: geoint

-- DROP DATABASE geoint;

CREATE DATABASE geoint
  WITH OWNER = g_geoint_a
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'English_United Kingdom.1252'
       LC_CTYPE = 'English_United Kingdom.1252'
       CONNECTION LIMIT = -1;
GRANT ALL ON DATABASE geoint TO g_geoint_a WITH GRANT OPTION;
GRANT ALL ON DATABASE geoint TO g_geoint WITH GRANT OPTION;
REVOKE ALL ON DATABASE geoint FROM public;

COMMENT ON DATABASE geoint
  IS 'GEOINT';

--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

-- Started on 2019-03-08 11:01:09

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 21963)
-- Name: ais; Type: SCHEMA; Schema: -; Owner: g_geoint_a
--

CREATE SCHEMA ais;


ALTER SCHEMA ais OWNER TO g_geoint_a;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 215 (class 1259 OID 21973)
-- Name: ais_fast; Type: TABLE; Schema: ais; Owner: geoint_admin
--

CREATE TABLE ais.ais_fast (
    ida bigint NOT NULL,
    ais_timestmp timestamp without time zone NOT NULL,
    ais_type smallint,
    mmsi bigint NOT NULL,
    lat real NOT NULL,
    lon real NOT NULL,
    navig_status smallint,
    rot real,
    sog real,
    cog real,
    heading smallint,
    posfix_type smallint,
    draught real,
    destination character varying
);


ALTER TABLE ais.ais_fast OWNER TO geoint_admin;

--
-- TOC entry 3580 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN ais_fast.ais_type; Type: COMMENT; Schema: ais; Owner: geoint_admin
--

COMMENT ON COLUMN ais.ais_fast.ais_type IS '1 "Class A", 2 "Class B"';


--
-- TOC entry 3581 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN ais_fast.lat; Type: COMMENT; Schema: ais; Owner: geoint_admin
--

COMMENT ON COLUMN ais.ais_fast.lat IS 'd.d WGS84';


--
-- TOC entry 3582 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN ais_fast.lon; Type: COMMENT; Schema: ais; Owner: geoint_admin
--

COMMENT ON COLUMN ais.ais_fast.lon IS 'd.d WGS84';


--
-- TOC entry 3583 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN ais_fast.navig_status; Type: COMMENT; Schema: ais; Owner: geoint_admin
--

COMMENT ON COLUMN ais.ais_fast.navig_status IS '0..15';


--
-- TOC entry 214 (class 1259 OID 21971)
-- Name: ais_fast_ida_seq; Type: SEQUENCE; Schema: ais; Owner: geoint_admin
--

CREATE SEQUENCE ais.ais_fast_ida_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ais.ais_fast_ida_seq OWNER TO geoint_admin;

--
-- TOC entry 3584 (class 0 OID 0)
-- Dependencies: 214
-- Name: ais_fast_ida_seq; Type: SEQUENCE OWNED BY; Schema: ais; Owner: geoint_admin
--

ALTER SEQUENCE ais.ais_fast_ida_seq OWNED BY ais.ais_fast.ida;


--
-- TOC entry 213 (class 1259 OID 21964)
-- Name: ais_raw; Type: TABLE; Schema: ais; Owner: geoint_admin
--

CREATE TABLE ais.ais_raw (
    ais_time character varying,
    ais_type character varying,
    mmsi bigint,
    lat real,
    lon real,
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
);


ALTER TABLE ais.ais_raw OWNER TO geoint_admin;

--
-- TOC entry 3585 (class 0 OID 0)
-- Dependencies: 213
-- Name: COLUMN ais_raw.lat; Type: COMMENT; Schema: ais; Owner: geoint_admin
--

COMMENT ON COLUMN ais.ais_raw.lat IS 'd.d WGS84';


--
-- TOC entry 3586 (class 0 OID 0)
-- Dependencies: 213
-- Name: COLUMN ais_raw.lon; Type: COMMENT; Schema: ais; Owner: geoint_admin
--

COMMENT ON COLUMN ais.ais_raw.lon IS 'd.d WGS84';


--
-- TOC entry 217 (class 1259 OID 22001)
-- Name: shpnms_scrp; Type: TABLE; Schema: ais; Owner: geoint_admin
--

CREATE TABLE ais.shpnms_scrp (
    ida integer NOT NULL,
    imo integer,
    mmsi integer,
    ship_name character varying,
    callsign character varying,
    ship_type character varying,
    flag character varying,
    ship_weight_gt character varying,
    ship_size_a integer,
    ship_size_b integer,
    xxx_year character varying,
    xxx_update_time character varying
);


ALTER TABLE ais.shpnms_scrp OWNER TO geoint_admin;

--
-- TOC entry 216 (class 1259 OID 21999)
-- Name: shpnms_scrp_ida_seq; Type: SEQUENCE; Schema: ais; Owner: geoint_admin
--

CREATE SEQUENCE ais.shpnms_scrp_ida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE ais.shpnms_scrp_ida_seq OWNER TO geoint_admin;

--
-- TOC entry 3588 (class 0 OID 0)
-- Dependencies: 216
-- Name: shpnms_scrp_ida_seq; Type: SEQUENCE OWNED BY; Schema: ais; Owner: geoint_admin
--

ALTER SEQUENCE ais.shpnms_scrp_ida_seq OWNED BY ais.shpnms_scrp.ida;


--
-- TOC entry 218 (class 1259 OID 22011)
-- Name: vestra_scrp; Type: TABLE; Schema: ais; Owner: geoint_admin
--

CREATE TABLE ais.vestra_scrp (
    shipname character varying,
    mmsi integer,
    imo integer NOT NULL,
    imovalid integer,
    callsign character varying,
    aistype character varying,
    shiplength real,
    shipwidth real,
    flag character varying
);


ALTER TABLE ais.vestra_scrp OWNER TO geoint_admin;

--
-- TOC entry 3423 (class 2604 OID 21976)
-- Name: ais_fast ida; Type: DEFAULT; Schema: ais; Owner: geoint_admin
--

ALTER TABLE ONLY ais.ais_fast ALTER COLUMN ida SET DEFAULT nextval('ais.ais_fast_ida_seq'::regclass);


--
-- TOC entry 3424 (class 2604 OID 22004)
-- Name: shpnms_scrp ida; Type: DEFAULT; Schema: ais; Owner: geoint_admin
--

ALTER TABLE ONLY ais.shpnms_scrp ALTER COLUMN ida SET DEFAULT nextval('ais.shpnms_scrp_ida_seq'::regclass);


--
-- TOC entry 3570 (class 0 OID 21973)
-- Dependencies: 215
-- Data for Name: ais_fast; Type: TABLE DATA; Schema: ais; Owner: geoint_admin
--

COPY ais.ais_fast (ida, ais_timestmp, ais_type, mmsi, lat, lon, navig_status, rot, sog, cog, heading, posfix_type, draught, destination) FROM stdin;
\.


--
-- TOC entry 3568 (class 0 OID 21964)
-- Dependencies: 213
-- Data for Name: ais_raw; Type: TABLE DATA; Schema: ais; Owner: geoint_admin
--

COPY ais.ais_raw (ais_time, ais_type, mmsi, lat, lon, navig_status, rot, sog, cog, heading, imo, callsign, ship_name, ship_type, cargo_type, ship_width, ship_length, posfix_type, draught, destination, eta, datasource) FROM stdin;
\.


--
-- TOC entry 3572 (class 0 OID 22001)
-- Dependencies: 217
-- Data for Name: shpnms_scrp; Type: TABLE DATA; Schema: ais; Owner: geoint_admin
--

COPY ais.shpnms_scrp (ida, imo, mmsi, ship_name, callsign, ship_type, flag, ship_weight_gt, ship_size_a, ship_size_b, xxx_year, xxx_update_time) FROM stdin;
\.


--
-- TOC entry 3573 (class 0 OID 22011)
-- Dependencies: 218
-- Data for Name: vestra_scrp; Type: TABLE DATA; Schema: ais; Owner: geoint_admin
--

COPY ais.vestra_scrp (shipname, mmsi, imo, imovalid, callsign, aistype, shiplength, shipwidth, flag) FROM stdin;
\.


--
-- TOC entry 3590 (class 0 OID 0)
-- Dependencies: 214
-- Name: ais_fast_ida_seq; Type: SEQUENCE SET; Schema: ais; Owner: geoint_admin
--

SELECT pg_catalog.setval('ais.ais_fast_ida_seq', 1, false);


--
-- TOC entry 3591 (class 0 OID 0)
-- Dependencies: 216
-- Name: shpnms_scrp_ida_seq; Type: SEQUENCE SET; Schema: ais; Owner: geoint_admin
--

SELECT pg_catalog.setval('ais.shpnms_scrp_ida_seq', 1, false);


--
-- TOC entry 3427 (class 2606 OID 21981)
-- Name: ais_fast ais_fast_pkey; Type: CONSTRAINT; Schema: ais; Owner: geoint_admin
--

ALTER TABLE ONLY ais.ais_fast
    ADD CONSTRAINT ais_fast_pkey PRIMARY KEY (ida);


--
-- TOC entry 3435 (class 2606 OID 22009)
-- Name: shpnms_scrp shipnames_pkey; Type: CONSTRAINT; Schema: ais; Owner: geoint_admin
--

ALTER TABLE ONLY ais.shpnms_scrp
    ADD CONSTRAINT shipnames_pkey PRIMARY KEY (ida);


--
-- TOC entry 3438 (class 2606 OID 22018)
-- Name: vestra_scrp vestra_pkey; Type: CONSTRAINT; Schema: ais; Owner: geoint_admin
--

ALTER TABLE ONLY ais.vestra_scrp
    ADD CONSTRAINT vestra_pkey PRIMARY KEY (imo);


--
-- TOC entry 3428 (class 1259 OID 21982)
-- Name: idx_fast_ais_type; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_fast_ais_type ON ais.ais_fast USING btree (ais_type);


--
-- TOC entry 3429 (class 1259 OID 21983)
-- Name: idx_fast_lat; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_fast_lat ON ais.ais_fast USING btree (lat);


--
-- TOC entry 3430 (class 1259 OID 21984)
-- Name: idx_fast_lon; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_fast_lon ON ais.ais_fast USING btree (lon);


--
-- TOC entry 3431 (class 1259 OID 21985)
-- Name: idx_fast_mmsi; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_fast_mmsi ON ais.ais_fast USING btree (mmsi);


--
-- TOC entry 3432 (class 1259 OID 21986)
-- Name: idx_fast_nav_stat; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_fast_nav_stat ON ais.ais_fast USING btree (navig_status);


--
-- TOC entry 3433 (class 1259 OID 21987)
-- Name: idx_fast_timestamp; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_fast_timestamp ON ais.ais_fast USING btree (ais_timestmp);


--
-- TOC entry 3425 (class 1259 OID 21970)
-- Name: idx_raw_nav_stat; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX idx_raw_nav_stat ON ais.ais_raw USING btree (navig_status);


--
-- TOC entry 3436 (class 1259 OID 22010)
-- Name: sns_imo; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX sns_imo ON ais.shpnms_scrp USING btree (imo);


--
-- TOC entry 3439 (class 1259 OID 22019)
-- Name: vts_imo; Type: INDEX; Schema: ais; Owner: geoint_admin
--

CREATE INDEX vts_imo ON ais.vestra_scrp USING btree (imo);


--
-- TOC entry 3579 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA ais; Type: ACL; Schema: -; Owner: g_geoint_a
--

GRANT USAGE ON SCHEMA ais TO g_geoint WITH GRANT OPTION;


--
-- TOC entry 3587 (class 0 OID 0)
-- Dependencies: 217
-- Name: TABLE shpnms_scrp; Type: ACL; Schema: ais; Owner: geoint_admin
--

REVOKE ALL ON TABLE ais.shpnms_scrp FROM geoint_admin;
GRANT ALL ON TABLE ais.shpnms_scrp TO geoint_admin WITH GRANT OPTION;
GRANT ALL ON TABLE ais.shpnms_scrp TO g_geoint WITH GRANT OPTION;


--
-- TOC entry 3589 (class 0 OID 0)
-- Dependencies: 218
-- Name: TABLE vestra_scrp; Type: ACL; Schema: ais; Owner: geoint_admin
--

REVOKE ALL ON TABLE ais.vestra_scrp FROM geoint_admin;
GRANT ALL ON TABLE ais.vestra_scrp TO geoint_admin WITH GRANT OPTION;
GRANT ALL ON TABLE ais.vestra_scrp TO g_geoint WITH GRANT OPTION;


-- Completed on 2019-03-08 11:01:09

--
-- PostgreSQL database dump complete
--

