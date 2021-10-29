from typing import List
import json
import os

from race_utils.candidate_group import Group
from candidate_utils.candidate import Candidate
from utils import read_json


class BaseRace(object):
    name: str = '比赛'
    groups: List[Group] = []

    def __init__(self):
        print('New race init: {}'.format(self.name))
        pass

    def setup_race(self):
        raise NotImplementedError

    def setup_group(self, name: int, length: int, candidates: List[Candidate]):
        raise NotImplementedError

    def dump(self) -> dict:
        dump = {'名称': self.name,
                '分组': [group.dump() for group in self.groups]}
        return dump

    def save_to_archive(self):
        path = os.path.join(os.getcwd(), 'documents', 'race_profile', '{}.json'
                            .format(self.name))
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.dump(), f, ensure_ascii=False)


def read_from_archive(path: str):
    return read_json(path)
