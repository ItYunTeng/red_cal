import pandas as pd
import sys

# file_old, file_new = input("输入新文件和处理后的文件全名: ").split()
file_old = ''
file_new = ''
# 处理参数
if len(sys.argv) > 2:
    file_old = sys.argv[1]
    file_new = sys.argv[2]
else:
    raise ValueError("Not enough arguments passed.")

# 读取 Excel 文件
df = pd.read_excel(file_old)

# 去除所有单元格中的换行符和头尾空格
df = df.applymap(lambda x: x.replace('\r\n', '').strip() if isinstance(x, str) else x)

# 保存修改后的文件
df.to_excel(file_new, index=False)
