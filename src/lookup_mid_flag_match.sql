select substring(mmsi::varchar, 1, 3), flag, count(*)
  from ais.ship_collect
  where mmsi is not null
    and mmsi != 0
  group by substring(mmsi::varchar, 1, 3), flag
  order by substring(mmsi::varchar, 1, 3), flag
  --limit 999
;

select distinct flag
  from ais.ship_collect
  order by flag
;