import datetime
import time
def showWord(s):
        print(s)


# name = "hello word"
# print(name)
# print(name * 2)
#
# listA = ["12", "34", 56]
# listB = ["123"]
# print(listA)
# print(listA[1:])
# print(listA + listB)
#
# # 字典  类似map
# mapA = {"name": "小芳", "age": 20}
# print(mapA)
#
# # 判断
# if True:
#     print(mapA['age'])
# else:
#     print("不输出")
#
# # 循环
# numList = [1, 2, 4, 6, 7, 9]
# a = []
# b = []
# while len(numList) > 0:
#     num = numList.pop()
#     if num % 2 == 0:
#         a.append(num)
#     else:
#         b.append(num)
#
# print(a)
# print(b)

a=123
c=False
i=isinstance(a,bool)
j=isinstance(c,bool)
print(i)
print(j)


print(1 + int("2"), 3, 4, 5)

b=0
while b<10:
        print(b,end=">")
        b=b+1
print()

date=datetime.date.today()
print(date)
print(date.ctime())
print(int(time.time()))