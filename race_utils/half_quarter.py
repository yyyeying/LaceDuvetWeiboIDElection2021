import os
import random
from typing import List

from candidate_race_utils.half_quarter import HalfQuarterCandidateRace
from candidate_utils.candidate import Candidate, read_from_archive
from race_utils.base import BaseRace
from race_utils.candidate_group import Group


class HalfQuarterRace(BaseRace):
    name: str = '1/8决赛'

    def __init__(self):
        super(HalfQuarterRace, self).__init__()

    def setup_race(self):
        profile_path = os.path.join(os.getcwd(), 'documents', 'candidate_profile')
        candidate_path_list = os.listdir(profile_path)
        candidate_list = []
        for path in candidate_path_list:
            candidate: Candidate = read_from_archive(os.path.join(profile_path, path))
            if candidate.race_history.group_race.win:
                candidate_list.append(candidate)
        random.shuffle(candidate_list)
        group = 65
        length = 2
        for i in range(8):
            candidates = [candidate_list.pop() for i in range(length)]
            print([candidate.name for candidate in candidates])
            self.setup_group(chr(group), length=length, candidates=candidates)
            group += 1

    def setup_group(self, name: str, length: int, candidates: List[Candidate]):
        new_group = Group(name=name, length=length)
        print(new_group)
        for i in range(length):
            candidate = candidates.pop()
            candidate.race_history.group_race = HalfQuarterCandidateRace(name)
            new_group.append_candidate(candidate)
            print(candidate.dump())
            candidate.save_to_archive()
        self.groups.append(new_group)
