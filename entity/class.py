class MyFirstClass:
    def __init__(self,name,age):
            self.name=name
            self.age=age

    def printInfo(self):
        print("我是"+self.name+"  年龄："+str(self.age))


x=MyFirstClass("zhangsan",12)
x.printInfo()
