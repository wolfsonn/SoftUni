from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        HotBeverage.__init__(self, name, price, milliliters)
