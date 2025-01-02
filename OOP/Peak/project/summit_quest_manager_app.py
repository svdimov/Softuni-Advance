

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from  project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAK_TYPE = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers:list[BaseClimber] = []
        self.peaks:list[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        climber = next((c for c in self.climbers if c.name == climber_name ),None)

        if climber is not None:
            return f"{climber_name} has been already registered."

        new_climber = self.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self,peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPE:
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.PEAK_TYPE[peak_type](peak_name,peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self,climber_name: str, peak_name: str, gear: list[str]):
        climber = next((c for c in self.climbers if c.name == climber_name),None)
        peaks = next((p for p in self.peaks if p.name == peak_name),None)

        require_gear = set(peaks.get_recommended_gear())
        missing_gear = require_gear - set(gear)

        if missing_gear:
            climber.is_prepared = False
            sort_gear = sorted(missing_gear)
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sort_gear)}."
        return  f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self,climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name),None)
        peaks = next((p for p in self.peaks if p.name == peak_name), None)

        if not climber:
            return f"Climber {climber_name} is not registered yet."

        if not peaks:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peaks)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peaks.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
    def get_statistics(self):
        sorted_climber = sorted([c for c in self.climbers if c.conquered_peaks],key=lambda c:(-len(c.conquered_peaks),c.name))
        result = [

            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"

        ]
        climber_statistic = "\n".join(str(c) for c in sorted_climber)
        result.append(climber_statistic)

        return '\n'.join(result)




