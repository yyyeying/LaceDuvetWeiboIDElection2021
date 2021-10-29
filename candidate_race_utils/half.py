from candidate_race_utils.base import BaseCandidateRace


class HalfCandidateRace(BaseCandidateRace):
    name: str = '半决赛'

    def __init__(self, group: str):
        super().__init__(group)