import os
from race_utils.base import read_from_archive
from race_utils.group import GroupRace

if __name__ == '__main__':
    group_race = read_from_archive(os.path.join(os.getcwd(), 'documents', 'race_profile', '小组赛.json'))
    print(group_race)
    for group in group_race['分组']:
        print('#### {}组\n'.format(group['名称']))
        for candidate in group['选手']:
            print('{}\n'.format(candidate['名称']))