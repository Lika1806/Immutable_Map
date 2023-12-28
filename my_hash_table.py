class Node:
    '''Represents an item of hash table'''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    '''Initializes a hash table with given size.'''
    def __init__(self, size):
        self.size = size
        self.__table = [None]*size
        self.__list = []
    
    def __len__(self):
        '''Returns a number of initialized items.'''
        return len(self.__list)

    def _hash(self, value):
        '''Hashes the value to get index.'''
        return hash(repr(value))%self.size

    def _find_key(self,node, key):
        '''Returns a key in the linked list of items with same hashed index starting from a given node, else returns None.'''
        while node:
            if node.key == key:
                return node
            node=node.next
        
    def __setitem__(self,key,value):
        '''Adds item if the key doen't exist, or updates the value of existing key.'''
        new_index = self._hash(key)
        if self.__table[new_index] is None:
            new_node = Node(key, value)
            self.__table[new_index] = new_node
            self.__list.append(new_node)
        else:
            node = self.__table[new_index]
            while node:
                if node.key == key:
                    node.value = value
                    break
                node = node.next
            else:
                node.next = Node(key, value)
                self.__list.append(node.next)
    
    def __getitem__(self,key):
        '''Returns the value associated with the key, 
        Raises KeyError if key doesn't exist.'''
        index = self._hash(key)
        result = self._find_key(self.__table[index], key)
        if result:
            return result.value
        raise KeyError("key doesn't exist")

    def __contains__(self, x):
        index = self._hash(x)
        return bool(self._find_key(self.__table[index], x))

    def __iter__(self):
        return iter(self.keys())


    def __delitem__(self, key):
        '''Deletes item assosiated with the givet key,
        Raises KeyError if key doesn't exist.'''
        index = self._hash(key)
        node = self.__table[index]
        prev_node = None
        while node:
            if node.key == key:
                if not prev_node:
                    self.__table[index] = node.next
                    return node
                prev_node.next = node.next
                return
            prev_node = node
            node=node.next
        raise KeyError("key doesn't exist")

    def __repr__(self):
        '''Returns a string representation of hashed table.'''
        nodes = [f"{repr(i.key)}: {i.value}" for i in self.__list]
        return '{' + ','.join(nodes)+'}'
 
    def get(self, key, default = None):
        try:
            result = self.__getitem__(key)
        except KeyError:
            result = default
        return result
        
    def items(self):
        return [(node.key, node.value) for node in self.__list]
    
    def keys(self):
        return [node.key for node in self.__list]
    
    def values(self):
        return [node.value for node in self.__list]


    

if __name__ == '__main__':
    a = MyHashTable(100)
    a[1] = 4
    a[2] = 5
    print(a)
    a['name'] = 'name'
    print(a['name'])
    a[1] = 78
    print(a)
    for i in a:
        print(i)