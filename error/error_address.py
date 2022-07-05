class AddressNeedToRunGetError(Exception):
    def __init__(self):
        super(AddressNeedToRunGetError, self).__init__('Need Run Address.get()')
