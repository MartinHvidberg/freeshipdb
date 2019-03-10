with mimo as (
select imo
  from ais.shpnms_scrp
  group by imo
  having count(*) > 4
  order by count(*) desc
)
select *
  from ais.shpnms_scrp
  where imo in (select imo from mimo)
    and imo != 0
  order by imo
;

with mimo as (
select imo
  from ais.vestra_scrp
  group by imo
  having count(*) > 1
  order by count(*) desc
)
select *
  from ais.vestra_scrp
  where imo in (select imo from mimo)
    and imo != 0
  order by imo
;