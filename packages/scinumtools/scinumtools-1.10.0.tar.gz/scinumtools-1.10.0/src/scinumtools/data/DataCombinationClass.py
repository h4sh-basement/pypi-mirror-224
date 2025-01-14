import itertools
from typing import Union

class DataCombination:
    _items: list
    
    def __init__(self, items):
        self._items = items

    def keys(self):
        ids = [range(len(item)) for item in self._items]
        for keys in itertools.product(*ids):
            yield keys
            
    def values(self):
        for values in itertools.product(*self._items):
            yield values
