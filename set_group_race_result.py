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
    '蕾丝糯米团子d酱': [18, True],
    '蕾丝包了d酱': [10, True],
    '蕾丝烧卖d酱': [8, False],
    '蕾丝锅盔d酱': [4, False],
    '蕾丝元宵d酱': [3, False]
}
result_d = {
    '蕾丝被子d酱': [14, True],
    '蕾丝包孓d酱': [6, True],
    '蕾丝麻酱糖饼d酱': [5, False],
    '蕾丝勾子d酱': [3, False],
    '蕾丝汤圆d酱': [3, False],
    '法蕾缝纫机d酱': [2, False]
}
result_h = {
    '蕾丝叉烧包d酱': [13, True],
    '蕾丝夹馍蘸大酱': [9, True],
    '蕾丝粽子d酱': [5, False],
    '蕾丝丸子d酱': [4, False],
    '蕾包子丝d酱': [4, False]
}

if __name__ == '__main__':
    group = 'H'
    set_race_result_by_group(group, result_h)
