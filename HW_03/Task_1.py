# Решить задачи, которые не успели решить на семинаре. 
# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.


def Task_1():
    friend1 = ['Иван', ('палатка', 'котелок', 'вода', 'шампура', 'покрывало', 'шашлык')]
    friend2 = ['Петор', ('палатка', 'покрывало', 'вода', 'топор', 'лопата')]
    friend3 = ['Влад', ('вода', 'покрывало', 'дрова', 'палатка', 'топор')]

    things = {friend1[0]: friend1[1]}
    things.update({friend2[0]: friend2[1]})
    things.update({friend3[0]: friend3[1]})

    set1 = set(things['Иван'])
    set2 = set(things['Петор'])
    set3 = set(things['Влад'])

    union_set = set(set1 | set2 | set3)
    print(f'\nВсе вещи: ', {*union_set},)
    print("*" * 130)
    other_set = set()
    for key in things:
        for other_key in things:
            if other_key != key:
                other_set.update(set(things[other_key]))
        print(f'Уникальные вещи {key} : {union_set - other_set}')
        other_set.clear()
    print("*" * 130)
    for key in things:
        print(f'{key} нет вещей: {union_set ^ set(things[key])}')

Task_1()