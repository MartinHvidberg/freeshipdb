INSERT INTO ais.imo (imo)
  SELECT imo 
  FROM ais.vestra_scrp
  group by imo
;

update ais.imo
  set source = 'vestra'
  where source is null
;

update ais.imo
  set last_seen = '2019-03-01'
  where source = 'vestra'
;

-------

INSERT INTO ais.imo (imo)
  SELECT imo 
  FROM ais.shpnms_scrp
  group by imo
;

update ais.imo
  set source = 'shpnms'
  where source is null
;

update ais.imo
  set last_seen = '2019-03-04'
  where source = 'shpnms'
;

------
select imo, count(*)
  from ais.imo
  group by imo
  order by count(*) desc
;

select source, count(*)
  from ais.imo
  group by source
  order by count(*) desc
;

select *
  from ais.imo
  where imo = 6721280
;