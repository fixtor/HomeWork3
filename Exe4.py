# Напишите программу, которая будет преобразовывать десятичное число в двоичное. # Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
temp_number = number
point = 1
division = 0


while temp_number > 0:
    division = division + temp_number %2 * point
    point *= 10
    temp_number = temp_number // 2

    
print(division)