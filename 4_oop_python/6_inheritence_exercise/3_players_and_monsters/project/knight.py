from project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        Hero.__init__(self, username, level)
