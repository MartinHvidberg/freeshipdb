select distinct flag
  from ais.ship_collect
  order by flag
;

select flag, substring(flag from 9 for 999), count(*)
  from ais.ship_collect
  where flag like 'Flag of %'
  group by flag
  order by flag
;

update ais.ship_collect
  set flag = substring(flag from 9 for 999)
  where flag like 'Flag of %'
;


select flag, substring(flag from 4 for 999), count(*)
  from ais.ship_collect
  where flag like 'of %'
  group by flag
  order by flag
;

update ais.ship_collect
  set flag = substring(flag from 4 for 999)
  where flag like 'of %'
;
