# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from uCreate_user_list import Int_list_create


list = Int_list_create()

sum = 0
i = 1
while i < len(list):
    sum += list[i]
    i += 2
print(sum)