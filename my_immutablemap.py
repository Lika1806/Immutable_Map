from collections.abc import Mapping
from typing import Sequence
from my_hash_table import MyHashTable

class MyImmutableMap:
    '''An immutable mapping type.'''
    def __init__(self, *args, **kwargs):
        '''initializes the immutable map.
        creates a Hash table with given arguments.'''
        if args and kwargs:
            raise ValueError("You can't pass *args an **kwargs together")
        elif  not args and not kwargs:
            raise ValueError("At least one argument is required")
        self.__dict = MyHashTable(100)
        if kwargs:
            pairs = kwargs.items()
        else:
                pairs = args
        for pair in pairs:
                if len(pair)!=2:
                    raise ValueError("Invalid Key-Value combination")
                self.__dict [pair[0]] = pair[1]

    def __len__(self):
        '''Returns the number of items.'''        
        return len(self.__dict)

    def __iter__(self):
        '''Returns an iteretor object over keys.'''        
        return iter(self.__dict)

    def __contains__(self, x):
        '''True if map has the specified key, else False.'''
        if x in self.__dict:
            return True
        return False
    
    def __eq__(self, other):
        '''Returns self == value'''
        if (isinstance(other,MyImmutableMap)):
            return len(self) == len(other) and sorted(self.items())== sorted(other.items())
        return NotImplemented

    def __getitem__ (self, key):
        '''x.__getitem__(y) <==> x[y]'''        
        return self.__dict[key]
    
    def __repr__(self):
        return repr(self.__dict)    
        
    def get(self, key, default = None):
        '''Returns the value for key if key is in map, else default.'''
        return self.__dict.get(key, default)
    
    def items(self):
        '''A set-like object providing a view on map's items.'''
        return self.__dict.items()
    
    def keys(self):
        '''A set-like object providing a view on map's keys.'''
        return self.__dict.keys()
    
    def values(self):
        '''A set-like object providing a view on map's values.'''        
        return self.__dict.values()
    




