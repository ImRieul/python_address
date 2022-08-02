# address package

[Kakao 주소 검색 개발 가이드](https://developers.kakao.com/tool/rest-api/open/get/v2-local-search-address.%7Bformat%7D)



### AnalyzeType

---

> 조건에 강한 정도입니다.

| Name    | Description                        |
|---------|------------------------------------|
| EXACT   | 강한 조건 검색, 도로명 + 건물명이 일치해야 검색됨      |
| SIMILAR | 약한 조건 검색, 도로명 + 건물명이 일치하지 않아도 검색 됨 |



### AddressType

---

> kakao Api 결과와 다르게 만들었습니다.
> 
> 도로같은 경우 도로명 주소가 없는데 이걸 구분하는 타입값이 없습니다.
> 
> 그래서 documents 안에 있는 address_type을 활용해 enum을 만들었습니다.
>
> REGION_ADDR, ROAD_ADDR는 기존 검색한 query에 대한 type을 나타내지만,
>
> AddressType은 class 안에 어떤 값이 있는지 나타냅니다.

| Name        | Description                  |
|-------------|------------------------------|
| REGION_ADDR | 지번 주소만 있음                    |
| ROAD_ADDR   | 지번 주소 + 도로명 주소가 있음           |
| NOT_EXIST   | 검색 결과가 없음(지번 주소, 도로명 주소가 없음) |
| BED_REQUEST | 잘못된 검색                       |



### AddressEnum

---

> 지번 주소에 관한 Enum

| Name                 | Description                   |
|----------------------|-------------------------------|
| ADDRESS_NAME         | 전체 지번 주소                      |
| REGION_1DEPTH_NAME   | 지역 1 Depth, 시도 단위             |
| REGION_2DEPTH_NAME   | 지역 2 Depth, 구 단위              |
| REGION_3DEPTH_NAME   | 지역 3 Depth, 동 단위              |
| REGION_3DEPTH_H_NAME | 지역 3 Depth, 행정동 명칭            |
| MAIN_ADDRESS_NO      | 지번 주번지                        |
| SUB_ADDRESS_NO       | 지번 부번지, 없을 경우 빈 문자열 반환('')    |
| B_CODE               | 법정코드                          |
| H_CODE               | 행정코드                          |
| MOUNTAIN_YN          | 산 여부 Y or N                   |
| X                    | X 좌표 값, 경위도인 경우 longitude(경도) |
| y                    | Y 좌표 값, 경위도인 경우 latitude(위도)  |


### RoadAddressEnum

---

> 도로명 주소에 관한 Enum

| Name               | Description                   |
|--------------------|-------------------------------|
| ADDRESS_NAME       | 전체 도로명 주소                     |
| REGION_1DEPTH_NAME | 지역명1                          |
| REGION_2DEPTH_NAME | 지역명2                          |
| REGION_3DEPTH_NAME | 지역명3                          |
| ROAD_NAME          | 도로명                           |
| MAIN_BUILDING_NO   | 건물 본번                         |
| SUB_BUILDING_NO    | 건물 부번, 없을 경우 빈 문자열 반환('')     |
| BUILDING_NAME      | 건물 이름                         |
| UNDERGROUND_YN     | 지하 여부, Y or N                 |
| ZONE_NO            | 우편번호(5자리)                     |
| X                  | X 좌표 값, 경위도인 경우 longitude(경도) |
| y                  | Y 좌표 값, 경위도인 경우 latitude(위도)  |
| FULL_NAME          | 전체 도로명 주소 (지역명3, 건물 이름)       |
