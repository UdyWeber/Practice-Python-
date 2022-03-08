from numpy import integer


Task = """Create a program that asks the user to enter their name and their age.
          Print out a message addressed to them that tells them the year that they will turn 100 years old.
          Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)"""
current_year = 2022

user_name = str(input("Type down your name: "))
user_age = int(input("Type down your age: "))

year_of_hundred_years = (current_year - user_age) + 100

print(f"Hey {user_name} i kwon that you have {user_age}, but have you realized that you are going to be a 100yo in {year_of_hundred_years}")
