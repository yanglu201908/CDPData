SELECT
  location_uuid as buildingUuid
    ,DATE_TRUNC('month', promos.report_month)::date AS month
    , COALESCE(SUM(promos.capacity), 0)             AS deskCapacity
    , COALESCE(SUM(promos.OCCUPANCY), 0)             AS deskOccupancy
    , 1.0 * (COALESCE(SUM(promos.OCCUPANCY), 0))
    / NULLIF((COALESCE(SUM(promos.capacity), 0)), 0) AS occupancyRate
    ,count(distinct promos.ACCOUNT_UUID) as countAccount
  ,(COALESCE(SUM(case when promos.account_name is null then 0 else promos.market_price_local end  ), 0))/nullif((COALESCE(SUM(promos.occupancy ), 0)),0) AS avgMarketPrice
  ,(COALESCE(SUM(promos.net_paid_price_local ), 0))/nullif((COALESCE(SUM(promos.occupancy ), 0)),0) AS avgNetPrice
    ,((COALESCE(SUM(promos.total_promo_discount_local ), 0)) + (COALESCE(SUM(promos.total_non_promo_discount_local ), 0)) +(COALESCE(SUM(promos.total_operational_discount_local ), 0)))*1.0/nullif((COALESCE(SUM(promos.local_currency_price ), 0)),0)  AS avgDiscount
FROM central.cdm.space_inventory_bom AS promos
left join china.china_dw.dim_locations_china AS location
ON promos.location_uuid = location.uuid
WHERE report_month >= TO_TIMESTAMP('2016-01-01')
and report_month <= current_date()
and location.COUNTRY ilike '%china%'
GROUP BY 1,2
order by 1,2