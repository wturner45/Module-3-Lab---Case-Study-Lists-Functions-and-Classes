# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # Call the superclass constructor
        super().__init__(vehicle_type)

        # Automobile attributes
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Method to display automobile information
    def display_info(self):
        print("\nVehicle Information")
        print("-------------------------")
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


# Main program
print("Enter the following information about your car:")

# Get user input
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an Automobile object
my_car = Automobile("car", year, make, model, doors, roof)

# Display automobile information
my_car.display_info()