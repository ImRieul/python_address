class AddressNeedToRunGetError(Exception):
    def __init__(self):
        super(AddressNeedToRunGetError, self).__init__('Need Run Address.get()')


class AddressAnalyzeTypeError(Exception):
    def __init__(self):
        super(AddressAnalyzeTypeError, self).__init__('class Address parameter analyze_type is only AnalyzeType Enum')


class AddressRoadAddressNotExist(Exception):
    def __init__(self):
        super(AddressRoadAddressNotExist, self).__init__('not exist road address name. just exist address name if is after search')
