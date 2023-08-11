__all__ = ["Farm"]

import random

from .animal_class import Animal
from .bird_class import Bird
from .dog_class import Dog
from .fish_class import Fish

_DOGS = [["Рэкс", 15, 3, "такса"], ["Лорд", 35, 2, "лабрадор"], ["Джек", 10, 4, "спаниэль"],
         ["Лайма", 12, 6, "лайка"], ["Лора", 11, 5, "такса"], ["Шарик", 8, 6, "пудель"],
         ["Буян", 45, 5, "овчарка"], ["Бек", 43, 5, "алабай"],
         ]

_FISH = [["Карп", 5, 2, "речной"], ["Лещ", 3, 1, "речной"], ["Щука", 5, 3, "речной"], ["Сом", 7, 3, "речной"],
         ["Осетр", 3, 1, "озерный"], ["Форель", 3, 1, "озерный"], ["Сельдь", 3, 1, "атлантическая"],
         ]

_BIRDS = [["Ушастый филин", 3, 1, "совиные", "у-ух"], ["Какаду", 3, 1, "попугай", "чирик"],
          ["Ворон черный", 3, 1, "вороновые", "кар"], ["Сорока", 3, 1, "вороновые", "кар"],
          ["Синица", 3, 1, "воробьиные", "чирик"], ["Зяблик", 3, 1, "воробьиные", "чирик"],
          ]


class Farm:
    def __init__(self):
        self._count_dog = 0
        self._count_fish = 0
        self._count_bird = 0

    def generate(self, animal_type: str) -> Animal:
        animal = None
        match animal_type.lower():
            case "dog":
                self._count_dog += 1
                animal = self._gen_dog()
            case "bird":
                self._count_bird += 1
                animal = self._gen_bird()
            case "fish":
                self._count_fish += 1
                animal = self._gen_fish()
        return animal

    def _gen_dog(self) -> Dog:
        dog = random.choice(_DOGS)
        return Dog(dog[0], dog[1], dog[2], dog[3])

    def _gen_bird(self) -> Bird:
        bird = random.choice(_BIRDS)
        return Bird(bird[0], bird[1], bird[2], bird[3], bird[4])

    def _gen_fish(self) -> Fish:
        fish = random.choice(_FISH)
        return Fish(fish[0], fish[1], fish[2], fish[3])

    def get_info(self):
        return f"собак: {self._count_dog}, птиц: {self._count_bird}, рыб: {self._count_fish}"
