from candidate_race_utils.base import BaseCandidateRace


class GroupCandidateRace(BaseCandidateRace):
    name: str = '小组赛'

    def __init__(self, group: str):
        super().__init__(group)
