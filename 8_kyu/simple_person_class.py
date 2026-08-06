# https://www.codewars.com/kata/55a144eff5124e546400005a

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
