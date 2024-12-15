# Method delegation
from collections import defaultdict

def normalize_key(key):
    return ''.join([char.lower() for char in key if char.isalpha()])

class NormalizedDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(normalize_key(key), value)
    
    def __getitem__(self, key):
        return super().__getitem__(normalize_key(key))




if __name__ == '__main__':
    scores = NormalizedDict()
    scores['Ada'] = 1_314
    scores['Carl'] = 1_236
    scores['Grace'] = 2_349

    print(scores)
    print(NormalizedDict.mro())