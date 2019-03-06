select imo/1000000, count(*)
  from ais.shpnms_scrp
  where imo > 999999 
    and imo < 10000000
  group by imo/1000000
  order by imo/1000000
  --limit 999
;

-- smaller
select count(*)
  from ais.shpnms_scrp
  where imo <= 999999
;

-- større
select count(*)
  from ais.shpnms_scrp
  where imo >= 10000000
;