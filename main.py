# 这是一个示例 Python 脚本。
from entity import student
from entity.student import Student


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
    x = 'sfv'
    print(f'{type(x)}')
    y = 1
    print(type(y))
    # 元祖中元素类型可不同 元素可重复
    x = (1, 1, 3, 5, '1')
    print(type(x))
    # 列表中的元素可重复，类型可不同
    y = [1, 1, 2, '1']
    print(type(y))
    # ‘'‘’’这个要对称
    s = '''this is a demo.'''
    # f = formate
    print(f'{s}')
    s = """W3cSchool"""
    print(s)
    print(s[0:-1])
    print(s[0])
    print(s[2:5])
    print(s[2:])
    print(s[1:5:2])
    print(s * 2)
    print(s + ' hello word')
    print('---------------------')
    print('hellow\nW3CSchool')
    # r=row让转义字符变成字符本身
    print(r'hellow\nW3CSchool')
    # 换两行
    print('\n' * 2)
    print(r'\n')


def input_test():
    input("this is a sample input message\n")
    # 接收收入的参数
    x = input("请输入x的值：")
    print(x)
    print(type(x))
    '''
    类似 x = intput("-----")
    x = int(x)
    '''
    x = int(input("请输入一个数值："))
    print(x)
    print(type(x))
    input("\n\n按下 enter 键后退出")


def print_test():
    x = "a"
    y = "b"
    print(x)
    print(y)
    print('-----------')
    print(x, end=" ")
    print(y, end=" ")
    print()


"""
按间距中的绿色按钮以运行脚本。
"""

'''
这是多行注释
'''
'''
Number 数字 值不可变
String 字符串 值不可变
List 列表 值可变
Tuple 元祖 值不可变
Set 集合 值可变
Dictionary 字典 值可变
'''

if __name__ == '__main__':
    print_hi('PyCharm')
    # input_test()
    print_test()
    std = Student(None, None)
    print(std)
    std1 = Student('狗哥', None)
    print(std1.name)
    std2 = Student('狗哥', 30)
    print(str(std2))

# 这是单行注释 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# 定义模型
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
 
# 连接数据库
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
 
# 按年龄升序排序
users_ascending = session.query(User).order_by(User.age.asc()).all()
 
# 按年龄降序排序
users_descending = session.query(User).order_by(User.age.desc()).all()
 
# 打印结果
for user in users_ascending:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
 
for user in users_descending:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
"""
