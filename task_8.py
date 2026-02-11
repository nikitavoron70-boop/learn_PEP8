def validate_age(age: int) -> str:
    MIN_AGE = 0
    MAX_AGE = 150
    ADULT_AGE = 18
    SENIOR_AGE = 65

    if MIN_AGE <= age <= MAX_AGE:
        if age < ADULT_AGE:
            return "minor"
        elif age < SENIOR_AGE:
            return "adult"
        else:
            return "senior"
    return "invalid"


x = 10
y = 20
z = 30

if x < y < z:
    print("Increasing sequence")