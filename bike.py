class Bike:
    ## Define constuctor for Bike
    def  __init__(self):
        self.bike_status = True 

    def is_working(self):
        print("bike is working")


class Docking:
    ## Set the constructor for this class
    def __init__(self):
        self.docked_bikes = []

    def release_bike(self):
        for ind, i in self.docked_bikes:
            if i.bike_status is True:
                print("Station will release")
                return self.docked_bikes.pop(ind)
        if not self.docked_bikes:
            print("There are no bikes to release")


    # for every docked bike in self.docked.bikes 
    # check the status
    # if bike is working then release
    # but if no bikes working or there are no bikes - then we want to return no bikes available 



    def dock_bike(self, bike, status):
        bike.bike_status = status
        self.docked_bikes.append(bike)

        
            
            


                        