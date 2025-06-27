class Vehicle:
    max_speed = 150

    def __init__(self, mileage: int):
        self.mileage = mileage
        self.gadgets = []

    def drive(self, distance):
        self.mileage += distance
        return f"Vehicle driven for {distance} km. Total mileage is now {self.mileage} km."

    def add_gadget(self, gadget_name):
        if gadget_name not in self.gadgets:
            self.gadgets.append(gadget_name)
            return f"Gadget '{gadget_name}' added."
        return f"Gadget '{gadget_name}' is already installed."

    def show_info(self):
        return f"Max Speed: {self.max_speed} km/h\nMileage: {self.mileage} km\nGadgets: {', '.join(self.gadgets) or 'None'}"


car = Vehicle(20)

print(car.show_info())
print(car.drive(80))
print(car.add_gadget("Hudly Wireless"))
print(car.add_gadget("Parking Sensor"))
print(car.add_gadget("Hudly Wireless"))
print(car.show_info())
