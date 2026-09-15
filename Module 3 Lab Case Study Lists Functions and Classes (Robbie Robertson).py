#Defines the Vehicle Class
class vehicle():
    def __init__(self, type):
        self.type = type

#Defines the Automobile Class and prints it's values
class automobile(vehicle):
    def __init__(self, type, year, model, doors, make, roof):
        super().__init__(type)
        self.year = year
        self.model = model
        self.doors = doors
        self.make = make
        self.roof = roof
        print(f"\nVehicle type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.doors}")
        print(f"Make: {self.make}")
        print(f"Type of Roof: {self.roof}")


def vehicleSelect():
    #Defines the Variables for the Vehicle Class
    vtype = input("Please input the type of vehicle such as car\n")
    while vtype.upper() != "CAR":
        vtype = input("Unsupported Vehicle Type\nPlease input the type of vehicle such as car\n")
    if vtype.upper() == "CAR":
        carDetails(vtype)

def carDetails(vtype):
    # Defines the Variables for the Automobile Class
    ayear = input("Please year of the car\n")
    amodel = input("Please input the model car\n")
    adoors = input("Please input whether the car has 2 or 4 doors\n")
    while adoors != "2" and adoors != "4":
        adoors = input("Unsupported number of doors\nPlease input whether the car has 2 or 4 doors\n")
    amake = input("Please input the make of the car\n")
    aroof = input("Please input if the car has a soild or sun roof\n")
    while aroof.upper() != "SOLID" and aroof.upper() != "SOLID ROOF" and aroof.upper() != "SUN ROOF" and aroof.upper() != "SUN":
        aroof = input("Unsupported roof type\nPlease input if the car has a soild or sun roof\n")
    automobile(vtype, ayear, amodel, adoors, amake, aroof)

#Calls the Vehicles Select Function
vehicleSelect()