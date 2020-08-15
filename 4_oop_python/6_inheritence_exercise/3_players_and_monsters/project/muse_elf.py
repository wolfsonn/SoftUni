from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        Elf.__init__(self, username, level)
