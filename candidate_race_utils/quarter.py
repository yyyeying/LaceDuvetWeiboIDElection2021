from candidate_race_utils.base import BaseCandidateRace


class QuarterCandidateRace(BaseCandidateRace):
    def __init__(self, group: str):
        super().__init__(group)