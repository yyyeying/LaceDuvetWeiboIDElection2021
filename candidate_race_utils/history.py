from candidate_race_utils.group import GroupCandidateRace
from candidate_race_utils.half_quarter import HalfQuarterCandidateRace
from candidate_race_utils.quarter import QuarterCandidateRace
from candidate_race_utils.half import HalfCandidateRace
from candidate_race_utils.final import FinalCandidateRace


class RaceHistory(object):
    group_race: GroupCandidateRace = None
    half_quarter_race: HalfQuarterCandidateRace = None
    quarter_race: QuarterCandidateRace = None
    half_race: HalfCandidateRace = None
    final_race: FinalCandidateRace = None

    def __init__(self):
        pass

    def get_history_str(self):
        info = ''
        for race in [self.group_race, self.half_quarter_race, self.quarter_race, self.half_race, self.final_race]:
            if race is not None:
                info += '{}: \n{}'.format(race.name, race.get_info_str())
        return info

    def dump(self) -> dict:
        dump = {}
        for race in [self.group_race, self.half_quarter_race, self.quarter_race, self.half_race, self.final_race]:
            if race is not None:
                dump.update({race.name: race.dump()})
        return dump
