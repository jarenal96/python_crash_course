from classcar import Car, ElectricCar

my_new_car = Car('audi','a4',2024)
print(f"{my_new_car.get_descriptive_name()}")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla','model 3',2024)
print(f"{my_tesla.get_descriptive_name()}")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
