from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list = []
        self.is_prepared: bool = True

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: " \
               f"{self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"
