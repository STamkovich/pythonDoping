# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания
dict1 = {1: 2, 2: 12, 3: 5, 4: 7, 5: 9, 6: 11}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get, reverse=True)

for e in sorted_keys:
    sorted_dict[e] = dict1[e]

print(sorted_dict)
