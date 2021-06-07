from typing import SupportsBytes


def madlib(name, subject):
    return f"{name}'s favorite subject in school is {subject}."

name = input("What is your name? ")
subject = input("What is your favorite subject? ")

print(madlib(name, subject))


