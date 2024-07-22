from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 2 * 20
        else:
            self.strength -= 1.5 * 20
        self.conquered_peaks.append(peak.name)


