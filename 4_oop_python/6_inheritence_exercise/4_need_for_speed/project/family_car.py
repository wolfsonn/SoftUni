from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        Car.__init__(self, fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
