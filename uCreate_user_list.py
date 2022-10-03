# Модуль для создания списков(изменяемые), кортежей(не изменяемы), словарей(изменяемые по ключу)


def Int_list_create():
    int_list = list(map(int,input('введите целые числа через пробел ').split()))
    return int_list


def Float_list_create():
    float_list = list(map(float,input('введите вещественные числа через пробел ').split()))
    return float_list