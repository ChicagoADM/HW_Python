# ✔Напишите однострочный генератор словаря, который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии
from pprint import pprint

NAMES = ["Иван", "Влад", "Петор", "Сергей"]
RATES = [15000, 23000, 18000, 40000]
PRIZE = ["10.25%", "17.00%", "8.50%", "11.70%"]


def gen_dict(names: list[str], rates: list[int], PRIZE: list[str]):
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, rates, map(lambda x: float(x[:-1]), PRIZE))))}


def main():
    print(NAMES)
    print(RATES)
    print(PRIZE)
    print(*gen_dict(NAMES, RATES, PRIZE))


main()