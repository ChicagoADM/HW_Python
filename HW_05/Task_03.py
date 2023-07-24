# ✔Создайте функцию генератор чисел Фибоначчи 

numbers = int(input("Введите количество чисел для генерации чисел Фибоначчи: "))
def get_fibonacci(num: int):
    f1, f2 = 0, 1
    for _ in range(num):
        yield f2
        f1, f2 = f2, f1 + f2

for i in get_fibonacci(numbers):
    print(i, end=', ')