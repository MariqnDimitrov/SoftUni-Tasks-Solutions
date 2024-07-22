from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=120)

    def miss(self, time_to_catch: int):
        reduced_oxygen = time_to_catch * 0.6
        if self.oxygen_level - reduced_oxygen < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduced_oxygen
            self.oxygen_level = int(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = 120

