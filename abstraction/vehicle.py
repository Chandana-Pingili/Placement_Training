from abstractVehicle import AbstractVehicle

class Bike(AbstractVehicle):
    def display_details(self):
        print("Bike details...")
        print(f"color : {self.colour}")
        print(f"number of tyres : {self.num_tyres}")
        print(f"number of gears : {self.gears}")

class Car(AbstractVehicle):
    def display_details(self):
        print("Car details...")
        print(f"color : {self.colour}")
        print(f"number of tyres : {self.num_tyres}")
        print(f"number of gears : {self.gears}")

class Scooty(AbstractVehicle):
    def display_details(self):
        print("Scooty details...")
        print(f"color : {self.colour}")
        print(f"number of tyres : {self.num_tyres}")
        print(f"number of gears : {self.gears}")

