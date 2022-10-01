# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: 
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil
from uCreate_user_list import Int_list_create


int_list = Int_list_create()
result = []              
n = math.ceil(len(int_list) / 2)
for i in range(n):
    result.append(int_list[i] * int_list[-i - 1])
print(result)
