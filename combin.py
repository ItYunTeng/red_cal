import itertools


def calc_ac_value(numbers):
    if len(numbers) != 6:
        raise ValueError("need input six red bool")
    numbers = sorted(numbers)
    differences = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            differences.append(numbers[j] - numbers[i])

    unique_differences = set(differences)
    ac_value = len(unique_differences) - (len(numbers) - 1)
    return ac_value


def clc_combin(els, num):
    for c in itertools.combinations(els, num):
        c = sorted(c)
        ac = calc_ac_value(c)
        if ac == 10:
            re = ','.join(str(v) for v in c)
            print(re, "||", ac)


items = [3, 6, 8, 10, 11, 12, 13, 15, 20, 21, 25, 28, 33]
r = 6
clc_combin(items, r)
