from enum import Enum


class AnalyzeType(Enum):
    EXACT = 'exact'
    SIMILAR = 'similar'


class AddressSearchType(Enum):
    REGION_ADDR = 'region_addr'
    ROAD_ADDR = 'road_address'
    NOT_EXIST = None
    BED_REQUEST = 'bed_request'


class AddressEnum(Enum):
    ADDRESS_NAME = 'address_name'
    REGION_1DEPTH_NAME = 'region_1depth_name'
    REGION_2DEPTH_NAME = 'region_2depth_name'
    REGION_3DEPTH_NAME = 'region_3depth_name'
    REGION_3DEPTH_H_NAME = 'region_3depth_h_name'
    MAIN_ADDRESS_NO = 'main_address_no'
    SUB_ADDRESS_NO = 'sub_address_no'
    B_CODE = 'b_code'
    H_CODE = 'h_code'
    MOUNTAIN_YN = 'mountain_yn'
    X = 'x'
    y = 'y'


class RoadAddressEnum(Enum):
    ADDRESS_NAME = 'address_name'
    REGION_1DEPTH_NAME = 'region_1depth_name'
    REGION_2DEPTH_NAME = 'region_2depth_name'
    REGION_3DEPTH_NAME = 'region_3depth_name'
    ROAD_NAME = 'road_name'
    MAIN_BUILDING_NO = 'main_building_no'
    SUB_BUILDING_NO = 'sub_building_no'
    BUILDING_NAME = 'building_name'
    UNDERGROUND_YN = 'underground_yn'
    ZONE_NO = 'zone_no'
    X = 'x'
    y = 'y'
    FULL_NAME = 'full_name'
