class Animal:

    def __init__(self, name: str, age: int, weight: float) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food: float) -> float:
        self.weight += food
        return self.weight

    def info(self) -> None:
        print(f"{self.name}, {self.age} years, {self.weight} kg")


class Cat(Animal):

    def __init__(self, name: str, age: int, weight: float, breed: str) -> None:
        super().__init__(name, age, weight)
        self.breed = breed

    def meow(self) -> None:
        print("MEOW!")


if __name__ == "__main__":
    animal = Animal("Бобик", 3, 15.5)
    animal.info()
    animal.eat(0.5)
    animal.info()

    cat = Cat("Мурка", 2, 4.2, "Сиамская")
    cat.info()
    cat.meow()
    print(f"Порода: {cat.breed}")