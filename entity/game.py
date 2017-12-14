# 猜数字游戏

# 初始化一个数字
import random

num = int(random.uniform(1, 100))

print("请输入一个数字")
m = int(input('输入整数：'))
while m != num:
    if m > num:
        print('输入的数字过大')
        m = int(input('输入整数：'))
    if m < num:
        print("输入的数字过小")
        m = int(input('输入整数：'))
    if m == num:
        print("输入正确答案是：", num, '  做的非常好')
        break
