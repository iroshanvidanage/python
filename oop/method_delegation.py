# Method delegation
from collections import defaultdict

def normalize_key(key):
    return ''.join([char.lower() for char in key if char.isalpha()])


class NormalizedDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(normalize_key(key), value)
    
    def __getitem__(self, key):
        return super().__getitem__(normalize_key(key))


class AdjustedValueDict(dict):
    def __init__(self, factor, *args, **kwargs):
        self.factor = factor
        super().__init__(*args, **kwargs)
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value * self.factor)


class PlayerScoreDict(NormalizedDict, AdjustedValueDict, defaultdict): ...

if __name__ == '__main__':
    scores = NormalizedDict()
    scores['Ada'] = 1_314
    scores['Carl'] = 1_236
    scores['Grace'] = 2_349

    print(scores)
    print(NormalizedDict.mro())

    scores1 = PlayerScoreDict(1_000, int)
    scores1['Ada'] = 1_314
    scores1['Carl'] = 1_236
    scores1['Grace'] = 2_349

    print(scores1)
    print('The value for Missing is: ', scores1['MISSING'])
    print(PlayerScoreDict.mro())