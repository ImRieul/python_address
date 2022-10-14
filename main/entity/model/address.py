from __future__ import annotations

from main.enums.address_enum import AddressDataType


class Address:
    def __init__(self,
                 region_1depth_name: str = None,
                 region_2depth_name: str = None,
                 dong_of_administration: str = None,
                 legal_dong: str = None,
                 road_name: str = None,
                 lot_main_number: str = None,
                 lot_sub_number: str = None,
                 road_main_number: str = None,
                 road_sub_number: str = None,
                 code_admin: str = None,
                 code_legal: str = None,
                 building_name: str = None,
                 postal_code: str = None,
                 x: str = None,
                 y: str = None,
                 is_mountain: bool = False,
                 is_underground: bool = False,
                 ):
        self.__region_1depth_name = region_1depth_name
        self.__region_2depth_name = region_2depth_name
        self.__dong_of_administration = dong_of_administration
        self.__legal_dong = legal_dong
        self.__road_name = road_name
        self.__lot_main_number = lot_main_number
        self.__lot_sub_number = lot_sub_number
        self.__road_main_number = road_main_number
        self.__road_sub_number = road_sub_number
        self.__code_admin = code_admin
        self.__code_legal = code_legal
        self.__building_name = building_name
        self.__postal_code = postal_code
        self.__x = x
        self.__y = y
        self.__is_mountain = is_mountain
        self.__is_underground = is_underground

    # init 변수에는 없음
    @property
    def lot_address(self) -> str:
        lot_number = ''
        if self.__lot_main_number is not None:
            lot_number += f' {self.__lot_main_number}'

        if self.__lot_sub_number is not None and self.__lot_main_number is not None:
            lot_number += f'-{self.__lot_sub_number}'

        return f'{self.__region_1depth_name} {self.__region_2depth_name} {self.__legal_dong}{lot_number}'

    # init 변수에는 없음
    @property
    def road_address(self) -> str:
        road_number = ''
        if self.__road_main_number is not None and self.__road_main_number != '':
            road_number += f' {self.__road_main_number}'

        if self.__road_sub_number is not None and self.__road_main_number != '' \
                and self.__road_sub_number is not None and self.__road_sub_number != '':
            road_number += f'번길 {self.__road_sub_number}'

        return f'{self.__region_1depth_name} {self.__region_2depth_name} {self.__road_name}{road_number}'

    @property
    def data_type(self) -> AddressDataType:
        """
        :return: AddressDataType.ALL_ADDR or AddressDataType.REGION_ADDR or AddressDataType.ROAD_ARR
        """
        if self.__dong_of_administration is not None:
            if self.__road_name is not None:
                return AddressDataType.ALL_ADDR
            else:
                return AddressDataType.REGION_ADDR
        else:
            if self.__road_name is not None:
                return AddressDataType.ROAD_ADDR
        return AddressDataType.NOT_EXIST

    @property
    def region_1depth_name(self) -> str:
        return self.__region_1depth_name

    @property
    def region_2depth_name(self) -> str:
        return self.__region_2depth_name

    @property
    def dong_of_administration(self) -> str:
        return self.__dong_of_administration

    @property
    def legal_dong(self) -> str:
        return self.__legal_dong

    @property
    def road_name(self) -> str:
        return self.__road_name

    @property
    def lot_main_number(self) -> str:
        return self.__lot_main_number

    @property
    def lot_sub_number(self) -> str:
        return self.__lot_sub_number

    @property
    def road_main_number(self) -> str:
        return self.__road_main_number

    @property
    def road_sub_number(self) -> str:
        return self.__road_sub_number

    @property
    def code_admin(self) -> str:
        return self.__code_admin

    @property
    def code_legal(self) -> str:
        return self.__code_legal

    @property
    def building_name(self) -> str:
        return self.__building_name

    @property
    def postal_code(self) -> str:
        return self.__postal_code

    @property
    def x(self) -> str:
        return self.__x

    @property
    def y(self) -> str:
        return self.__y

    @property
    def is_mountain(self) -> bool:
        return self.__is_mountain

    @property
    def is_underground(self) -> bool:
        return self.__is_underground

    @region_1depth_name.setter
    def region_1depth_name(self, value: str):
        self.__region_1depth_name = value

    @region_2depth_name.setter
    def region_2depth_name(self, value: str):
        self.__region_2depth_name = value

    @dong_of_administration.setter
    def dong_of_administration(self, value: str):
        self.__dong_of_administration = value

    @legal_dong.setter
    def legal_dong(self, value: str):
        self.__legal_dong = value

    @road_name.setter
    def road_name(self, value: str):
        self.__road_name = value

    @lot_main_number.setter
    def lot_main_number(self, value: str):
        self.__lot_main_number = value

    @lot_sub_number.setter
    def lot_sub_number(self, value: str):
        self.__lot_sub_number = value

    @road_main_number.setter
    def road_main_number(self, value: str):
        self.__road_main_number = value

    @road_sub_number.setter
    def road_sub_number(self, value: str):
        self.__road_sub_number = value

    @code_admin.setter
    def code_admin(self, value: str):
        self.__code_admin = value

    @code_legal.setter
    def code_legal(self, value: str):
        self.__code_legal = value

    @building_name.setter
    def building_name(self, value: str):
        self.__building_name = value

    @postal_code.setter
    def postal_code(self, value: str):
        self.__postal_code = value

    @x.setter
    def x(self, value: str):
        self.__x = value

    @y.setter
    def y(self, value: str):
        self.__y = value

    @is_mountain.setter
    def is_mountain(self, value: bool):
        self.__is_mountain = value

    @is_underground.setter
    def is_underground(self, value: bool):
        self.__is_underground = value

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)
