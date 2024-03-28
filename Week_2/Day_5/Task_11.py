class Vehicle():
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)


class ElectricCar(Car):
    def __init__(self, make, model, year, fuel_type, battery_capacity):
        super().__init__(make, model, year, fuel_type)
        self.battery_capacity = battery_capacity

    def show(self):
        print(
            f"The car make is {self.make}, model {self.model}, year {self.year}, fuel_type {self.fuel_type}, with battery_capacity of {self.battery_capacity}")


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year, fuel_type)


class HybridTruck(Truck):
    def __init__(self, make, model, year, fuel_type, electric_motor_power):
        super().__init__(make, model, year, fuel_type)
        self.electric_motor_power = electric_motor_power

    def show(self):
        print(f"The truck is {self.make}, model {self.model}, year {self.year}, fuel_type {self.fuel_type}, with electric_motor_power of {self.electric_motor_power}")


if __name__ == "__main__":
    vehicle = Vehicle("Toyota", "SUV", 2021, "Petrol")

    # For ElectricCar and HybridTruck instances, now we need to pass all required arguments including the new ones specific to their type.
    electric_car = ElectricCar("Tesla", "Model S", 2020, "Electric", "100kWh")
    hybrid_truck = HybridTruck("Ford", "F-150", 2021, "Hybrid", "35kW")

    electric_car.show()
    hybrid_truck.show()
