import os
import json

from candidate_utils.category import CandidateCategory
from candidate_race_utils.history import RaceHistory
from utils import read_json

from candidate_race_utils.group import GroupCandidateRace
from candidate_race_utils.half_quarter import HalfQuarterCandidateRace
from candidate_race_utils.quarter import QuarterCandidateRace
from candidate_race_utils.half import HalfCandidateRace
from candidate_race_utils.final import FinalCandidateRace


class Candidate(object):
    number: int = 0
    name: str = None
    category: CandidateCategory = None
    race_history: RaceHistory = RaceHistory()

    def __init__(self, number: int, name: str, category: CandidateCategory = None):
        self.number = number
        self.name = name
        self.category = category
        self.race_history = RaceHistory()

    def dump(self) -> dict:
        dump = {'编号': self.number,
                '名称': self.name,
                '类别': self.category.value,
                '比赛信息': self.race_history.dump()}
        return dump

    def save_to_archive(self):
        path = os.path.join(os.getcwd(), 'documents', 'candidate_profile', '{}-{}.json'
                            .format(self.number, self.name))
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.dump(), f, ensure_ascii=False)


def read_from_archive(path: str):
    return read_from_json(read_json(path))


race_dict = {'小组赛': GroupCandidateRace,
             '1/8决赛': HalfQuarterCandidateRace,
             '八分之一决赛': HalfQuarterCandidateRace,
             '1/4决赛': QuarterCandidateRace,
             '四分之一决赛': QuarterCandidateRace,
             '半决赛': HalfCandidateRace,
             '决赛': FinalCandidateRace}


def read_from_json(candidate_json: dict):
    # print(candidate_json)
    category = None
    for c in CandidateCategory:
        if c.value == candidate_json['类别']:
            category = c
    candidate = Candidate(number=candidate_json['编号'],
                          name=candidate_json['名称'],
                          category=category)
    for race_name, race_info in candidate_json['比赛信息'].items():
        new_race = race_dict[race_name](group=race_info['组别'])
        new_race.set_score(race_info['票数'])
        new_race.set_result(race_info['结果'])
        if race_name == '小组赛':
            candidate.race_history.group_race = new_race
        elif race_name == '1/8决赛' or race_name == '八分之一决赛':
            candidate.race_history.half_quarter_race = new_race
        elif race_name == '1/4决赛' or race_name == '四分之一决赛':
            candidate.race_history.quarter_race = new_race
        elif race_name == '半决赛':
            candidate.race_history.half_race = new_race
        elif race_name == '决赛':
            candidate.race_history.final_race = new_race
    return candidate
