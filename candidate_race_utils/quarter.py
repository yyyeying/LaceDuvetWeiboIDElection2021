from candidate_race_utils.base import BaseCandidateRace


class QuarterCandidateRace(BaseCandidateRace):
    name: str = '四分之一决赛'

    def __init__(self, group: str):
        super().__init__(group)
