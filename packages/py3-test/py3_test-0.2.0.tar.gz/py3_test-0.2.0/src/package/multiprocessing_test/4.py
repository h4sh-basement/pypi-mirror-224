"""
@author: lijc210@163.com
@file: 4.py
@time: 2019/11/14
@desc: 功能描述。
"""


class Father:
    def __init__(self, name):
        self.name = name
        print("name: %s" % (self.name))

    def getName(self):
        return "Father " + self.name


class Son(Father):
    def __init__(self, name):
        super().__init__(name)
        print("hi")
        self.name = name

    def getName(self):
        return "Son " + self.name


if __name__ == "__main__":
    son = Son("runoob")
    print(son.getName())
