from candidate_utils import set_race_result_by_group, get_candidate_info_by_group

result_c = {
    '蕾丝流心奶黄包d酱': [19, True],
    '蕾丝面条炸酱': [12, True],
    '蕾丝傻子d酱': [9, False],
    '蕾丝勺子d酱': [2, False],
    '蕾丝雹子d酱': [3, False],
    '蕾丝包孑d酱': [2, False]
}
result_g = {
    '糯米团子d酱': [18, True],
    '蕾丝包了d酱': [10, True],
    '蕾丝烧卖d酱': [8, False],
    '蕾丝锅盔d酱': [4, False],
    '蕾丝元宵d酱': [3, False]
}

if __name__ == '__main__':
    group = 'G'
    set_race_result_by_group(group, result_g)
