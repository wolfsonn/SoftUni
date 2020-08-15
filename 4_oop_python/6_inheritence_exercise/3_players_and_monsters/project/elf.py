from project.hero import Hero


class Elf(Hero):
    def __init__(self, username, level):
        Hero.__init__(self, username, level)

