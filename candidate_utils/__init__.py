from candidate_utils.category import CandidateCategory
from candidate_utils.candidate import Candidate


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
            new_candidate.print_profile()
            new_candidate.save_to_archive()
            number += 1
