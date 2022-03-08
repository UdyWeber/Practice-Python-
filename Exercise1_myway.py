from datetime import date


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def year_of_hundred_years_old(self) -> int:
        current_year = date.today().year
        born_year = current_year - self.age
        year_of_100_years_old = born_year + 100

        return year_of_100_years_old

def create_person() -> Person:
    person_name = str(input("Please inform the persons name: "))
    person_age = int(input("Please inform the persons age: "))

    person = Person(person_name, person_age)
    return person

person = create_person()

print(f"{person.name.capitalize()} youre going to be a hundred years old in the year {person.year_of_hundred_years_old()}")

