from typing import Iterable
from forbiddenfruit import curse


def joint(value: int, __iterable: Iterable[int]) -> int:
    """
    Concatenate any number of integers **without addition**.

    The int whose method is called is inserted in between each given int. The result is returned as a new int.

    Example:
    a = 69
    a.joint([1, 2, 3]) -> 69123
    """
    
    v = str(value)
    for i in __iterable: v+= str(i)
    return int(v)

curse(int, 'joint', joint)
