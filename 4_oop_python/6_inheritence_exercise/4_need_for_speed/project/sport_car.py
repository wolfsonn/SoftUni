from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        Car.__init__(self, fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
