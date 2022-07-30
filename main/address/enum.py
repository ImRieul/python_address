from enum import Enum


class AnalyzeType(Enum):
    EXACT = 'exact'
    SIMILAR = 'similar'


class AddressType(Enum):
    REGION_ADDR = 'region_addr'
    ROAD_ADDR = 'road_address'
    BED_REQUEST = 'bed_request'
    NOT_EXIST = None
