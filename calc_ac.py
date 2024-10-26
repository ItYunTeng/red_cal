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
