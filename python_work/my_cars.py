#from car import Car,ElectricCar
import car

#my_beetle=Car('volkswagen','beetle',2019)
my_beetle=car.Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

#my_tesla=ElectricCar('twsla','roadster',2019)
my_tesla=car.ElectricCar('twsla','roadster',2019)
print(my_tesla.get_descriptive_name())