from project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        Beverage.__init__(self, name, price, milliliters)
