select LOCATION_UUID as buildingUuid
    ,CONFERENCE_ROOM_UUID as conferenceRoomUuid
    ,CONFERENCE_ROOM_NAME as conferenceRoomName
    ,ROOM_CAPACITY as conferenceRoomCapacity
    ,sum(datediff('minute',RESERVATION_START_TIME,RESERVATION_END_TIME))/60 as weeklyBookedHours
from CHINA.CHINA_DW.CHINA_CONFERENCE_ROOM_RESERVATION_DTL
where RESERVATION_START_TIME < date_trunc('week',current_date())
and   RESERVATION_START_TIME >= dateadd('day',-7,date_trunc('week',current_date()))
and   RESERVATION_IS_WEEKDAY = 1
and   CANCELLED_AT is null
and   LOC_COUNTRY ilike '%china%'
group by 1,2,3,4
order by 1,2