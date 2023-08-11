from .animal_class import Animal

__all__ = ["Dog"]


class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self) -> str:
        return "Run"

    def say(self):
        return "Gov"

    def __str__(self):
        return f"{super().__str__()}, {self.dog_type}"
