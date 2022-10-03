# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from uCreate_user_list import Float_list_create


float_list = Float_list_create()


new_list = []
for i in range(len(float_list)):
    new_list.append(round((float_list[i] - int(float_list[i])), 3))


print(max(new_list) - min(new_list))
