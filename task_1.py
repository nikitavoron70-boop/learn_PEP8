import math
from typing import Union


def calculate_even_powers_sum(x: Union[int, float], y: Union[int, float]) -> float:
    MAX_POWER = 8

    result = sum(
        math.pow(x, power) / math.factorial(power)
        for power in range(0, MAX_POWER + 1, 2)
    )

    return float(result + y)