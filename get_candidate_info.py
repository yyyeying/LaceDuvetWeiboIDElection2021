import os

from candidate_utils.candidate import read_from_archive, Candidate

if __name__ == '__main__':
    profile_path = os.path.join(os.getcwd(), 'documents', 'candidate_profile')
    candidate_path_list = os.listdir(profile_path)
    for path in candidate_path_list:
        candidate: Candidate = read_from_archive(os.path.join(profile_path, path))
        print(candidate.dump())