from .animal_class import Animal

__all__ = ["Fish"]


class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self) -> str:
        return "Swim"

    def say(self) -> str:
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"
