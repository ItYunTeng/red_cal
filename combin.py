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


items = [17, 11, 21, 31, 12, 22, 32, 3, 13, 23, 33, 24, 6, 16, 26, 8, 18, 28, 10, 20, 30, 29]
r = 6
clc_combin(items, r)
