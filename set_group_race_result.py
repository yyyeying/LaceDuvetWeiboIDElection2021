from candidate_utils import set_race_result_by_group, get_candidate_info_by_group

if __name__ == '__main__':
    group = 'E'
    result = {'蕾丝傻狍子d酱': [34, True],
              '蕾丝馒头d酱': [9, True],
              '蕾丝豆汁d酱': [7, False],
              '蕾丝包包d酱': [6, False],
              '蕾包丝子d酱': [2, False]}
    set_race_result_by_group(group, result)
