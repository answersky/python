
# 99乘法表
# 定义两个list
list1=[]
list2=[]
i=1
while i<10:
    list1.append(i)
    list2.append(i)
    i=i+1
print(list1)
print(list2)

for k in list1:
    for j in list2:
        if j<=k:
            print(k,"*",j,"=",k*j,end=" ")
    print()