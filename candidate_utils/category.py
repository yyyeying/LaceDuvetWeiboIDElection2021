from enum import Enum


class CandidateCategory(Enum):
    FOOD_WITH_FILLING = '带馅儿食物类'
    FOOD_WITHOUT_FILLING = '不带馅儿食物类'
    SIMILIAR_PRONOUNCIATION = '谐音类'
    SIMILIAR_CHARACTER = '形近字类'
    RAMDOM_SHIT = '排列组合类'
    ORIGINAL_TRANSLATION = '忠实翻译类'
    MENTAL_ISSUE = '精神病类'