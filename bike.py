class Bike:
    def is_working(self):
        print("bike is working")


class Docking:
    def docking_release(self):
        print("Station will release")
        return Bike()