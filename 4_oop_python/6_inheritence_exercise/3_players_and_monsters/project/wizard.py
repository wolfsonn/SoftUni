from project.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        Hero.__init__(self, username, level)
