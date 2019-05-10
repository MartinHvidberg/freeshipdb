-- only IMO count
select imo, count(*)
  from ais.ship_collect
  group by imo
  order by count(*) desc
;
select imo, mmsi, count(*)
  from ais.ship_collect
  group by imo, mmsi
  order by count(*) desc
;

select *
  from ais.ship_collect
  where imo = 0
    and mmsi = 0
;

with psbt as (
select imo, mmsi, count(*)
  from ais.ship_collect
  where mmsi != 0
    and mmsi is not null
  group by imo, mmsi
  order by count(*) desc
)
select mmsi, count(*)
  from psbt
  group by mmsi
  having count(*) > 1
  order by count(*) desc
;

select *
  from ais.ship_collect
  where imo = 9496848
;
