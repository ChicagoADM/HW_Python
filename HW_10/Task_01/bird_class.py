from .animal_class import Animal

__all__ = ["Bird"]


class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self.sound = sound

    def move(self) -> str:
        return "Fly"

    def say(self) -> str:
        return self.sound

    def __str__(self):
        return f"{super().__str__()}, {self.bird_type}"
