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
        self._region_1depth_name = region_1depth_name
        self._region_2depth_name = region_2depth_name
        self._dong_of_administration = dong_of_administration
        self._legal_dong = legal_dong
        self._road_name = road_name
        self._lot_main_number = lot_main_number
        self._lot_sub_number = lot_sub_number
        self._road_main_number = road_main_number
        self._road_sub_number = road_sub_number
        self._code_admin = code_admin
        self._code_legal = code_legal
        self._building_name = building_name
        self._postal_code = postal_code
        self._x = x
        self._y = y
        self._is_mountain = is_mountain
        self._is_underground = is_underground

    # init 변수에는 없음
    @property
    def lot_address(self) -> str:
        lot_number = ''
        if self._lot_main_number != '' \
                and self._lot_main_number is not None:
            lot_number += f' {self._lot_main_number}'

        if self._lot_sub_number != '' \
                and self._lot_main_number != '' \
                and self._lot_sub_number is not None \
                and self._lot_main_number is not None:
            lot_number += f'-{self._lot_sub_number}'

        return f'{self._region_1depth_name} {self._region_2depth_name} {self._legal_dong}{lot_number}'

    # init 변수에는 없음
    @property
    def road_address(self) -> str:
        road_number = ''
        if self._road_main_number is not None and self._road_main_number != '':
            road_number += f' {self._road_main_number}'

        if self._road_sub_number is not None and self._road_main_number != '' \
                and self._road_sub_number is not None and self._road_sub_number != '':
            road_number += f'번길 {self._road_sub_number}'

        return f'{self._region_1depth_name} {self._region_2depth_name} {self._road_name}{road_number}'

    @property
    def road_address_fullname(self) -> str:
        name = self.road_address
        if self._legal_dong != '':
            name += f' ({self._legal_dong}'

            if self._building_name != '':
                name += f', {self._building_name}'

            name += ')'

        return name

    @property
    def data_type(self) -> AddressDataType:
        """
        :return: AddressDataType.ALL_ADDR or AddressDataType.REGION_ADDR or AddressDataType.ROAD_ARR
        """
        if self._dong_of_administration is not None:
            if self._road_name is not None:
                return AddressDataType.ALL_ADDR
            else:
                return AddressDataType.REGION_ADDR
        else:
            if self._road_name is not None:
                return AddressDataType.ROAD_ADDR
        return AddressDataType.NOT_EXIST

    @property
    def region_1depth_name(self) -> str:
        return self._region_1depth_name

    @property
    def region_2depth_name(self) -> str:
        return self._region_2depth_name

    @property
    def dong_of_administration(self) -> str:
        return self._dong_of_administration

    @property
    def legal_dong(self) -> str:
        return self._legal_dong

    @property
    def road_name(self) -> str:
        return self._road_name

    @property
    def lot_main_number(self) -> str:
        return self._lot_main_number

    @property
    def lot_sub_number(self) -> str:
        return self._lot_sub_number

    @property
    def road_main_number(self) -> str:
        return self._road_main_number

    @property
    def road_sub_number(self) -> str:
        return self._road_sub_number

    @property
    def code_admin(self) -> str:
        return self._code_admin

    @property
    def code_legal(self) -> str:
        return self._code_legal

    @property
    def building_name(self) -> str:
        return self._building_name

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @property
    def x(self) -> str:
        return self._x

    @property
    def y(self) -> str:
        return self._y

    @property
    def is_mountain(self) -> bool:
        return self._is_mountain

    @property
    def is_underground(self) -> bool:
        return self._is_underground

    @region_1depth_name.setter
    def region_1depth_name(self, value: str):
        self._region_1depth_name = value

    @region_2depth_name.setter
    def region_2depth_name(self, value: str):
        self._region_2depth_name = value

    @dong_of_administration.setter
    def dong_of_administration(self, value: str):
        self._dong_of_administration = value

    @legal_dong.setter
    def legal_dong(self, value: str):
        self._legal_dong = value

    @road_name.setter
    def road_name(self, value: str):
        self._road_name = value

    @lot_main_number.setter
    def lot_main_number(self, value: str):
        self._lot_main_number = value

    @lot_sub_number.setter
    def lot_sub_number(self, value: str):
        self._lot_sub_number = value

    @road_main_number.setter
    def road_main_number(self, value: str):
        self._road_main_number = value

    @road_sub_number.setter
    def road_sub_number(self, value: str):
        self._road_sub_number = value

    @code_admin.setter
    def code_admin(self, value: str):
        self._code_admin = value

    @code_legal.setter
    def code_legal(self, value: str):
        self._code_legal = value

    @building_name.setter
    def building_name(self, value: str):
        self._building_name = value

    @postal_code.setter
    def postal_code(self, value: str):
        self._postal_code = value

    @x.setter
    def x(self, value: str):
        self._x = value

    @y.setter
    def y(self, value: str):
        self._y = value

    @is_mountain.setter
    def is_mountain(self, value: bool):
        self._is_mountain = value

    @is_underground.setter
    def is_underground(self, value: bool):
        self._is_underground = value

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)
