class UserData:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"User: {self.name}, Age: {self.age}"

    def __repr__(self) -> str:
        return f"UserData(name='{self.name}', age={self.age})"


def get_adult_user_names(users: list[UserData]) -> list[str]:
    ADULT_AGE = 18
    return [user.name.upper() for user in users if user.age > ADULT_AGE]


if __name__ == "__main__":
    users = [
        UserData("Иван", 25),
        UserData("Мария", 17),
        UserData("Алексей", 30),
    ]

    print("Все пользователи:")
    for user in users:
        print(user)

    adult_names = get_adult_user_names(users)
    print(f"\nСовершеннолетние: {adult_names}")