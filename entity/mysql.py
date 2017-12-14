import pymysql
# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="123",database="xwcms",charset="utf8")
index=db.cursor()

# 执行sql
index.execute("select * from account")

# 获取结果
result=index.fetchall()
print(result)

index.close()