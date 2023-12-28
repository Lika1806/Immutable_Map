from my_immutablemap import MyImmutableMap

def test_print(instance, key):
    try:
        print(f'{key} = {instance[key]}')
    except KeyError:
        print(f"key {key} wasn't found")

def test_get(instance, key, default = None):
    try:
        print(f'{key} = {instance[key]}')
    except KeyError:
        print(f"key {key} wasn't found")

def test_contains(instance, key):
    if key in instance:
        print(f'{key} is in {instance}')
    else:
        print(f'{key} is not in {instance}')

def test_eq(instance1, instance2):
    if instance1==instance2:
        print(f'{instance1} is equal to {instance2}')
        return
    print(f'{instance1} is not equal to {instance2}')


if(__name__ == '__main__'):
    print("--------------")
    print("Creating instances")
    my_map1 = MyImmutableMap(('a',111), ('b',222), ('c',333))
    my_map2 = MyImmutableMap(['a', 111])
    my_map3 = MyImmutableMap(a=333, b=111, c=222)
    try:
        my_map4 = MyImmutableMap()
    except ValueError as e:
        print(f'error "{e}" is succsessfully detected') 
    try:
        my_map4 = MyImmutableMap(('a', 111), b=222)
    except ValueError as e:
        print(f'error "{e}" is succsessfully detected')
    try:
        my_map4 = MyImmutableMap(['a', (111,222),2])
    except ValueError as e:
        print(f'error "{e}" is succsessfully detected')          

    print("--------------")
    print("Testing repr")
    print(my_map1)
    print(my_map2)
    print(my_map3)

    print("--------------")
    print("Testing getitem function")
    test_print(my_map1,'a')
    test_print(my_map1,'d')

    print("--------------")
    print("Testing get funtion")

    test_get(my_map1, 'b')
    test_get(my_map1, 'e')

    print("--------------")
    print("Testing len function")
    print(len(my_map1))

    print("--------------")
    print("Testing contains function")
    test_contains(my_map1,'a')
    test_contains(my_map1,'f')

    print("--------------")
    print("Gettin items")
    print(my_map1.items())

    print("--------------")
    print("Gettin keys")
    print(my_map1.keys())

    print("--------------")
    print("Gettin values")
    print(my_map1.values())

    print("--------------")
    print("Iterating through map")
    for i in my_map1:
        print(i)

    print("--------------")
    print("Testing __eq__ function")
    test_eq(my_map1, my_map2)
    test_eq(my_map1, my_map3)

