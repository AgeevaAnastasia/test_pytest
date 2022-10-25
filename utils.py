def division(a, b):
    return a / b


def mult_30_not_105_not_15(number):
    if number % 30 != 0:
        if number % 5 == 0 and number % 10 == 0 or number % 15 == 0:
            return True
    return False


def multiply_1_to_n(num):
    mult = 1
    lst1 = []
    for i in range(1, num + 1):
        mult *= i
        lst1.append(mult)
    return lst1


def find_number_inlist(list_string, number):
    for item in list_string:
        if number in item:
            return True



def summ_odd_indexes(l):
    summ = 0
    for i in range(len(l)):
        if i % 2 == 1:
            summ += l[i]
    return summ


def sum_of_pairs(lst):
    lst1 = []
    for i in range((len(lst) + 1) // 2):
        lst1.append(lst[i] * lst[-1 - i])
    return lst1
