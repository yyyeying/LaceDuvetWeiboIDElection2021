import os
from candidate_utils import generate_candidate_profile

if __name__ == '__main__':
    source = os.path.join(os.getcwd(), 'documents', 'candidates.txt')
    dest = os.path.join(os.getcwd(), 'documents', 'candidate_profile')
    generate_candidate_profile(source, dest)