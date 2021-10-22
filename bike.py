class Bike:
    def is_working(self):
        print("bike is working")


class Docking:
    def __init__(self):
        self.docked_bikes = []

    def release_bike(self):
        if not self.docked_bikes:
            print("There are no bikes to release")
        else:
            print("Station will release")
            return self.docked_bikes.pop()
        

    def dock_bike(self, bike):
        self.docked_bikes.append(bike)        