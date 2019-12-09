select
     uuid as buildingUuid
    ,name as buildingNameEng
    ,BUILDING_NAME_CHINESE as buildingNameChn
    ,city as buildingCity
    ,latitude
    ,longitude
    ,ADDRESS_CHINESE as addressChn
    ,DIVISION_NAME as districtName
    ,OPENED_ON_LOCAL as buildingOpenDate
    ,amenities
from CHINA.CHINA_DW.DIM_LOCATIONS_CHINA