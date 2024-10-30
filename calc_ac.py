# def calc_ac_value(numbers):
#     if len(numbers) != 6:
#         raise ValueError("必须输入6个红球")
#     numbers = sorted(numbers)
#     differences = []
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             differences.append(numbers[j] - numbers[i])
#
#     unique_differences = set(differences)
#     ac_value = (max(numbers) - min(numbers) - len(unique_differences))
#     return ac_value
#
#
# reds = []
# ac = calc_ac_value(reds)
# print(f"AC值: {ac}")

# 创建一个2维列表
matrix = [[0 for col in range(4)] for row in range(3)]

# 创建一个3维列表
cube = [[[0 for depth in range(2)] for col in range(4)] for row in range(3)]

# 打印多维列表
print(matrix)  # 输出: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(
    cube)  # 输出: [[[0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0]]]


def func(a, b, c):
    print(a, b, c)


args = (1, 2, 3)
func(*args)  # 输出 1 2 3


# 单星号（*）用于将元组解包成函数参数。例如，如果你有一个元组和一个接受多个参数的函数，你可以使用单星号在调用函数时解包元组。
def func(a, b, c):
    print(a, b, c)


kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)  # 输出 1 2 3


# 双星号（**）用于将字典解包成关键字参数。例如，如果你有一个字典并且想要将其作为关键字参数传递给一个函数，你可以使用双星号。
def func(*args, **kwargs):
    print(args)
    print(kwargs)


# 这些操作通常用于函数调用时参数的解包。在函数定义中，星号和双星号用于表示任意数量的位置参数和关键字参数。
func(1, 2, 3, a=4, b=5)
# 输出
# (1, 2, 3)
# {'a': 4, 'b': 5}
