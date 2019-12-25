select LOCATION_UUID as buildingUuid
    ,loc_name as buildingName
    ,case when ROOM_CAPACITY <= 4 then 'small (2:4)'
          when ROOM_CAPACITY > 4 and ROOM_CAPACITY <= 10 then 'medium (5:10)'
          when ROOM_CAPACITY > 10 and ROOM_CAPACITY <= 17 then 'large (11:17)'
          when ROOM_CAPACITY > 17 then 'classroom (18+)' end as roomType
    ,CONFERENCE_ROOM_NAME as roomName
    ,ROOM_CAPACITY as roomCapacity
    ,date_trunc('day',RESERVATION_START_TIME)::date as startDate
    ,TO_CHAR(CAST(RESERVATION_START_TIME AS timestamp), 'DY') as startWeekday
-- 	,EXTRACT(HOUR FROM RESERVATION_START_TIME) AS startHour
    ,RESERVATION_START_TIME
    ,RESERVATION_END_TIME
--     ,sum(datediff('minute',RESERVATION_START_TIME,RESERVATION_END_TIME))/60 as BookedHours
from CHINA.CHINA_DW.CHINA_CONFERENCE_ROOM_RESERVATION_DTL
where RESERVATION_START_TIME < current_date()
and   RESERVATION_START_TIME >= dateadd('day',-90,current_date())
and   CANCELLED_AT is null
and   LOC_COUNTRY = 'China'
-- group by 1,2,3,4,5,6,7,8
order by 1,2,3,4,5,6,7