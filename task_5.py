from typing import Optional

def check_values(a: Optional[bool], b: Optional[bool]) -> Optional[int]:
    if a is True and b is False:
        return True
    elif a is None or b is None:
        return None

    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


flag = True
while flag:
    flag = False

x = 1 + 2 * 3 - 4 / 5
list1 = [1, 2, 3, 4, 5]
dict1 = {'a': 1, 'b': 2, 'c': 3}


def func(x: float = 0, y: float = 0) -> float:
    return x ** 2 + y ** 2


result = func(x=2, y=3)
if 10 < result < 20:
    print("Result in range")