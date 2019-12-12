select distinct
         loc.UUID as buildingUuid
        ,loc.NAME as buildingName
        ,date_trunc('day',e.START_DATETIME)::date as eventDate
        ,e.UUID as eventUuid
        ,e.name as eventName
        ,e.event_type as eventType
        ,ATTENDANCES_COUNT as rsvp
from FIVETRAN.MENA_PUBLIC.EVENTS e
left join FIVETRAN.MENA_PUBLIC.LOCATIONS loc on loc.id = e.location_id
where loc.COUNTRY ilike '%china%'
order by 1,2,3,4