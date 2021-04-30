from car import Car

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!!")

my_tesla=ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()