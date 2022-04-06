from datetime import date

muca = "Muca é gay"

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

    person = Person(name=person_name,age=person_age)
    return person

person = create_person()
person_list = []
response = "S"

while response in "Ss":
    print(f"{person.name.capitalize()} youre going to be a hundred years old in the year {person.year_of_hundred_years_old()}")
    person_info_tuple = (person.name.capitalize(), person.year_of_hundred_years_old())
    person_list.append(person_info_tuple)
    response = str(input("Do you whanna continue[S/N]: "))
    if response in "Nn":
        break
    person = create_person()
