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
    reds = []
    for c in itertools.combinations(els, num):
        c = sorted(c)
        ac = calc_ac_value(c)
        if ac <= 8 or ac >= 6:
            re = ','.join(str(v) for v in c)
            red = re + '||' + str(ac) + "\n"
            reds.append(red)
    # 打开文件，并写入内容
    with open("files/ac.txt", "w") as f:
        f.writelines(reds)


items = [
    10, 20, 30, 1, 11, 21, 31, 2, 12, 22, 32, 3, 13, 23, 33, 6, 16, 26, 9, 19,
    29, 4, 14, 24, 8, 18, 28
]
r = 6
clc_combin(items, r)
