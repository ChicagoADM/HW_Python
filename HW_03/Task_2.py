# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов. 

list_1 = [7, 1, 2, 3, 6, 5, 8, 2, 1, 5, 7, 9, 10]

def set_element(list_element):
    count = 0
    set_list_element = []

    for i in list_element:
        for j in list_element:
            if i == j:
                count += 1
                if j not in set_list_element and count > 1:
                    set_list_element.append(j)
        count = 0
    return set_list_element

print(f"Список дублирующихся элементов без дубликатов {set_element(list_1)}")