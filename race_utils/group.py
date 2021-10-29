import random
import os
from typing import List

from candidate_utils.candidate import Candidate, read_from_archive
from race_utils.base import BaseRace
from race_utils.candidate_group import Group
from candidate_race_utils.group import GroupCandidateRace


class GroupRace(BaseRace):
    name: str = '小组赛'

    def __init__(self):
        super(GroupRace, self).__init__()

    def setup_race(self):
        profile_path = os.path.join(os.getcwd(), 'documents', 'candidate_profile')
        candidate_path_list = os.listdir(profile_path)
        candidate_list = []
        for path in candidate_path_list:
            candidate: Candidate = read_from_archive(os.path.join(profile_path, path))
            candidate_list.append(candidate)
        random.shuffle(candidate_list)
        group = 65
        # print(group)
        length = 6
        for i in range(4):
            candidates = [candidate_list.pop() for i in range(length)]
            print([candidate.name for candidate in candidates])
            self.setup_group(chr(group), length=length, candidates=candidates)
            group += 1
        length = 5
        for i in range(4):
            candidates = [candidate_list.pop() for i in range(length)]
            self.setup_group(chr(group), length=length, candidates=candidates)
            group += 1

    def setup_group(self, name: str, length: int, candidates: List[Candidate]):
        new_group = Group(name=name, length=length)
        print(new_group)
        for i in range(length):
            candidate = candidates.pop()
            candidate.race_history.group_race = GroupCandidateRace(name)
            new_group.append_candidate(candidate)
            print(candidate.dump())
            candidate.save_to_archive()
        self.groups.append(new_group)

