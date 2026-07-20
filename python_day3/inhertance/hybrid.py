class Device:
    def power_on(self):
        print("Device powered on.")

class Camera(Device):
    def take_photo(self):
        print("Photo taken.")

class Phone(Device):
    def make_call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("Browsing internet...")

smartphone = SmartPhone()
smartphone.power_on()
smartphone.take_photo()
smartphone.make_call()
smartphone.browse_internet()