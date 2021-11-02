from candidate_utils import set_race_result_by_group, get_candidate_info_by_group

if __name__ == '__main__':
    group = 'F'
    result = {'蕾丝狍子d酱': [13, True],
              '蕾丝肘子d酱': [12, True],
              'd丝酱包子雷': [8, False],
              '蕾丝糯米鸡d酱': [8, False],
              '蕾丝馄饨d酱': [6, False],
              '蕾丝馅儿饼d酱': [1, False]}
    set_race_result_by_group(group, result)
