from utils import ip_get_location


class Data(object):
    location = ip_get_location.get_location()

    def get_location(self):
        return Data.location

    def set_location(self):
        Data.location = ip_get_location.get_location()

    pass
