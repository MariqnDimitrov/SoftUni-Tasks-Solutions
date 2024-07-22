from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.base_peak import BasePeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        valid_climber_types = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
        all_climbers_names = [c.name for c in self.climbers]
        if climber_name in all_climbers_names:
            return f"{climber_name} has been already registered."
        elif climber_type in valid_climber_types:
            climber = valid_climber_types[climber_type](climber_name)
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."
        return f"{climber_type} doesn't exist in our register."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        valid_peaks = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
        if peak_type in valid_peaks:
            peak = valid_peaks[peak_type](peak_name, peak_elevation)
            self.peaks.append(peak)
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."
        return f"{peak_type} is an unknown type of peak."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next(c for c in self.climbers if c.name == climber_name)
        peak = next(p for p in self.peaks if p.name == peak_name)
        recommended_gear = peak.get_recommended_gear()
        if recommended_gear == gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        missing_gear = [g for g in recommended_gear if g not in gear]
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: " \
               f"{', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber_names = [c.name for c in self.climbers]
        peak_names = [p.name for p in self.peaks]
        if climber_name not in climber_names:
            return f"Climber {climber_name} is not registered yet."
        if peak_name not in peak_names:
            return f"Peak {peak_name} is not part of the wish list."
        climber = next(c1 for c1 in self.climbers if c1.name == climber_name)
        peak = next(p1 for p1 in self.peaks if p1.name == peak_name)
        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers_with_peaks = [climber for climber in self.climbers if climber.conquered_peaks != []]
        sorted_climbers = list(filter(lambda x: (-len(x.conquered_peaks), x.name), climbers_with_peaks))
        result = f"Total climbed peaks: {len(self.peaks)}\n"
        result += "**Climber's statistics:**\n"
        for climber in sorted_climbers:
            if len(climber.conquered_peaks) > 1:
                climber.conquered_peaks = sorted(climber.conquered_peaks)
        str_climbers = [str(c) for c in sorted_climbers]
        result += "\n".join(str_climbers)
        return result
