from candidate_utils import set_race_result_by_group, get_candidate_info_by_group

result = {"A": {
    '蕾丝馒头d酱': [5, False],
    '蕾丝傻狍子d酱': [21, True]
    },
    "B":{
    '蕾丝糯米团子d酱': [21, True],
    '蕾丝叉烧包d酱': [5, False]
    },
    "C": {
        '蕾丝狍子d酱': [12, True],
    '蕾丝包纸d酱': [7, False]
    },
    "D": {
        '蕾丝包了d酱': [3, False],
    '蕾丝纸包不住火d酱': [16, True]
    }}

if __name__ == '__main__':
    for group, r in result.items():
        print(group)
        print(r)
        set_race_result_by_group(group=group, result=r)
        get_candidate_info_by_group(group)
