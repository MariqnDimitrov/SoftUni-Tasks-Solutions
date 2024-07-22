from typing import List
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    appropriate_divers = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    appropriate_fishes = {"PredatoryFish": PredatoryFish,"DeepSeaFish": DeepSeaFish}

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.appropriate_divers.keys():
            return f"{diver_type} is not allowed in our competition."
        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."
        new_diver = self.appropriate_divers[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.appropriate_fishes.keys():
            return f"{fish_type} is forbidden for chasing in our competition."
        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."
        new_fish = self.appropriate_fishes[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        current_diver = ""
        current_fish = ""
        fish_found = False
        diver_found = False
        for diver in self.divers:
            if diver.name == diver_name:
                diver_found = True
                current_diver = diver
        if not diver_found:
            return f"{diver_name} is not registered for the competition."
        for fish in self.fish_list:
            if fish.name == fish_name:
                fish_found = True
                current_fish = fish
        if not fish_found:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if current_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if current_diver.oxygen_level < current_fish.time_to_catch:
            current_diver.miss(current_fish.time_to_catch)
            if current_diver.oxygen_level <= 0:
                current_diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        if current_diver.oxygen_level == current_fish.time_to_catch:
            if is_lucky:
                current_diver.hit(current_fish)
                if current_diver.oxygen_level <= 0:
                    current_diver.update_health_status()
                return f"{diver_name} hits a {current_fish.points}pt. {fish_name}."
            else:
                current_diver.miss(current_fish.time_to_catch)
                if current_diver.oxygen_level <= 0:
                    current_diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        if current_diver.oxygen_level > current_fish.time_to_catch:
            current_diver.hit(current_fish)
            if current_diver.oxygen_level == 0:
                current_diver.update_health_status()
            return f"{diver_name} hits a {current_fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                divers_recovered += 1
        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = next(d for d in self.divers if d.name == diver_name)
        fish_details = [f.fish_details() for f in diver.catch]
        result = f"**{diver_name} Catch Report**\n"
        result += '\n'.join(fish_details)
        return result

    def competition_statistics(self):
        result = "**Nautical Catch Challenge Statistics**\n"
        divers_in_good_health = [d for d in self.divers if not d.has_health_issue]
        filtered_divers = list(filter(lambda x: (-x.competition_points, len(x.catch), x.name), divers_in_good_health))
        diver_statistics = [diver.__str__() for diver in filtered_divers]
        result += "\n".join(diver_statistics)
        return result

nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())


















