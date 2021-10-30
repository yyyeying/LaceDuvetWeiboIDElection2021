import os

from candidate_utils import get_candidate_info_by_group

if __name__ == '__main__':
    candidates = get_candidate_info_by_group('all')
    for candidate in candidates:
        print(candidate.dump())
