import os
from typing import Dict, List, Union

from candidate_utils.category import CandidateCategory
from candidate_utils.candidate import Candidate, read_from_archive


def generate_candidate_profile(source: str = './documents/candidate.txt', dest: str = './documents/candidate_profile'):
    lines = []
    with open(source, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    category = None
    number = 1
    for line in lines:
        line = line.replace('\n', '')
        # print(line)
        if '*' in line:
            for c in CandidateCategory:
                # print(c.value)
                if c.value == line.replace('*', ''):
                    category = c
        else:
            new_candidate = Candidate(number=number, name=line, category=category)
            print(new_candidate.dump())
            new_candidate.save_to_archive()
            number += 1


def get_candidate_info_by_group(group: str):
    profile_path = os.path.join(os.getcwd(), 'documents', 'candidate_profile')
    candidate_path_list = os.listdir(profile_path)
    candidate_list = []
    for path in candidate_path_list:
        candidate: Candidate = read_from_archive(os.path.join(profile_path, path))
        if group == 'all':
            candidate_list.append(candidate)
        elif candidate.race_history.group_race.group == group:
            candidate_list.append(candidate)
    return candidate_list


def set_race_result_by_group(group: str, result: Dict[str, List[Union[int, bool]]]):
    candidate_list = get_candidate_info_by_group(group)
    for candidate in candidate_list:
        print(candidate.dump())
    for name, score in result.items():
        print("{}, {}".format(name, score))
        for candidate in candidate_list:
            # print(candidate.name)
            if candidate.name == name:
                # print(candidate.name)
                candidate.race_history.group_race.set_score(score[0])
                candidate.race_history.group_race.set_result(score[1])
    for candidate in candidate_list:
        print(candidate.dump())
        candidate.save_to_archive()
