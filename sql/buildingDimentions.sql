with member_gender as
         (
             select LOCATION_CODE
                  , LOCATION_NAME
                  , count(distinct uuid)                                      as count_member
                  , count(distinct case when GENDER = 'Female' then uuid end) as count_female
                  , count(distinct case when GENDER = 'Male' then uuid end)   as count_male
                  , count(distinct case when GENDER is null then uuid end)    as count_unknown
             from CHINA.CHINA_DW.CHINA_OS_FACT_USERS_SNOWFLAKE
             where IS_ACTIVE_FULLTIME_MEMBER = true
               and CREATE_DATE = (select max(CREATE_DATE) from CHINA.CHINA_DW.CHINA_OS_FACT_USERS_SNOWFLAKE)
               and LOCATION_COUNTRY ilike '%china%'
             group by 1, 2
         )


select
     uuid as buildingUuid
    ,name as buildingNameEng
    ,BUILDING_NAME_CHINESE as buildingNameChn
    ,city as buildingCity
    ,latitude
    ,longitude
    ,ADDRESS_CHINESE as addressChn
    ,ADDRESS_LINE1
    ,ADDRESS_LINE2
    ,DIVISION_NAME as districtName
    ,null as commercialName
    ,OPENED_ON_LOCAL as Date
    ,amenities
    ,TRANSPORTATIONS
    ,b.count_female / b.count_member as female_pct
    ,b.count_male / b.count_member as male_pct
    ,b.count_unknown / b.count_member as unknown_pct
from CHINA.CHINA_DW.DIM_LOCATIONS_CHINA a
left join member_gender b on a.NAME = b.LOCATION_NAME