class BaseCandidateRace(object):
    name: str = '比赛'
    group: str = None
    finish: bool = False
    score: int = 0
    win: bool = False

    def __init__(self, group: str):
        self.group = group

    def set_score(self, score: int):
        self.score = score

    def set_result(self, result: bool):
        self.win = result
        self.finish = True

    def dump(self) -> dict:
        dump = {'组别': self.group,
                '票数': self.score,
                '结果': self.win
                }
        return dump
