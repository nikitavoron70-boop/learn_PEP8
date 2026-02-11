import time
from typing import Any, Callable


def timer(func: Callable) -> Callable:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        elapsed_time = end - start
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds")

        return result

    return wrapper


@timer
def heavy_computation(n: int) -> int:
    return sum(i * i for i in range(n))


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
filtered = list(filter(lambda x: x > 10, squared))