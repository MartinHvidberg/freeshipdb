select count(*)
  from (
  select distinct (imo, mmsi), count(*)
    from ais.aisdk_190401
    where latitude <= 90
      and longitude <= 180
    group by imo, mmsi
    order by count(*) desc
    --limit 99
  ) as imos
;