# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

negative_fib = [1, 0]
for i in range(7):
    negative_fib.insert(0, negative_fib[1] - negative_fib[0])
for i in range(8):
    negative_fib.append(negative_fib[-2] + negative_fib[-1])

print(negative_fib)
