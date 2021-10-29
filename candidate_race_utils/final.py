from candidate_race_utils.base import BaseCandidateRace


class FinalCandidateRace(BaseCandidateRace):
    name: str = '决赛'

    def __init__(self, group: str):
        super().__init__(group)