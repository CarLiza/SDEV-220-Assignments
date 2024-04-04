class Vehicle:

    def __init__(self, type):
        self.type = type
    
    def get_type(self):
        print("Vehicle type:", self.type)

class Automobile(Vehicle):

    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Ask for the type of the car
newcar = input("What is the type of the car: ")
#car1 = Vehicle(newcar)

#add the features of the car
info_car = []
v_year = int(input("The year of the vehicle: "))
v_make = input("Make of the vehicle: ")
v_model = input("Model of the vehicle: ")
v_doors = int(input("How many doors does the car have? "))
v_roof = input("Is the roof solid or sun roof? ")
car1_1 = Automobile(newcar, v_year,v_make,v_model,v_doors,v_roof)
info_car.append(car1_1)

car1_1.get_type()

for i in info_car:
    print("Year:",i.year)
    print("Make:",i.make)
    print("Model:",i.model)
    print("Number of doors:",i.doors)
    print("Type of roof:",i.roof)