# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list.insert(2, 400)
del my_list[6]
print(my_list)