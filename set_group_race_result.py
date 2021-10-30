from candidate_utils import set_race_result_by_group, get_candidate_info_by_group

if __name__ == '__main__':
    group = 'A'
    result = {'蕾丝香河肉饼d酱': [1, False],
              '蕾丝卤煮d酱': [2, False],
              '蕾包丝子d酱': [3, False],
              '蕾丝包孑d酱': [4, False],
              '蕾丝包孓d酱': [5, True],
              '蕾丝汤圆d酱': [6, True]}
    set_race_result_by_group(group, result)
