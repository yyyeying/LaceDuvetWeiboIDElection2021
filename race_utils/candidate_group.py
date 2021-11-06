from typing import List

from candidate_utils.candidate import Candidate


class Group(object):
    name: str = None
    length: int = 0
    candidates: List[Candidate] = []

    def __init__(self, name: str, length: int):
        self.name = name
        self.length = length
        self.candidates = []
        print('New group init: name: {}, length: {}'.format(self.name, self.length))

    def append_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)
        print('Group {} append candidate: {}, length: {}'
              .format(self.name, candidate.name, len(self.candidates)))

    def dump(self) -> dict:
        dump = {'名称': self.name,
                '选手': [{'编号': candidate.number,
                        '名称': candidate.name}
                       for candidate in self.candidates]}
        return dump
