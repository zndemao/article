
class Locad_Page:
    def __init__(self):
        self.location = ip_get_location.get_location()


    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = ip_get_location.get_location()
    pass

from utils import ip_get_location

location = ip_get_location.get_location()
print(location)