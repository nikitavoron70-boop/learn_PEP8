numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n * n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]


def generate_data(n: int) -> list[int]:
    return [i * 2 for i in range(n) if i > 0]


data = generate_data(100)
filtered = [x for x in data if x % 10 == 0]