from candidate_race_utils.base import BaseCandidateRace


class HalfQuarterCandidateRace(BaseCandidateRace):
    name: str = '八分之一决赛'

    def __init__(self, group: str):
        super().__init__(group)