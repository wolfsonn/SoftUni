from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        Wizard.__init__(self, username, level)
