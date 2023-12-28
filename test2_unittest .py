import unittest
from my_immutablemap import MyImmutableMap

class TestMyImmutableMap(unittest.TestCase):

    def setUp(self):
        self.my_map1 = MyImmutableMap(('a',111), ('b',222), ('c', 333))
        self.my_map2 = MyImmutableMap(['a',111], ['b',222], ['c', 333])
        self.my_map3 = MyImmutableMap(a=333, b=111, c=222)
        with self.assertRaises(ValueError):
            my_map4 = MyImmutableMap()        
        with self.assertRaises(ValueError):
            my_map4 = MyImmutableMap(('a', 111), b=222)
        with self.assertRaises(ValueError):
            my_map4 = MyImmutableMap(['a', (111,222),2])     

    def test_print(self):
        self.assertEqual(self.my_map1['a'], 111)
        with self.assertRaises(KeyError):
            value = self.my_map1['d']

    def test_get(self):
        self.assertEqual(self.my_map1.get('b'), 222)
        self.assertIsNone(self.my_map1.get('e'))

    def test_len(self):
        self.assertEqual(len(self.my_map1), 3)

    def test_contains(self):
        self.assertIn('a', self.my_map1)
        self.assertNotIn('f', self.my_map1)

    def test_items(self):
        self.assertEqual(list(self.my_map1.items()), [('a', 111), ('b', 222), ('c', 333)])

    def test_keys(self):
        self.assertEqual(set(self.my_map1.keys()), {'a', 'b', 'c'})

    def test_values(self):
        self.assertEqual(set(self.my_map1.values()), {111, 222, 333})

    def test_iteration(self):
        keys = []
        for key in self.my_map1:
            keys.append(key)
        self.assertEqual(keys, ['a', 'b', 'c'])

    def test_eq(self):
        self.assertEqual(self.my_map1, self.my_map2)
        self.assertNotEqual(self.my_map1, self.my_map3)

if __name__ == '__main__':
    unittest.main()