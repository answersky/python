import socket
import sys

# 创建socket对象
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 获取本机地址
host=socket.gethostname()
port=9999

# 端口绑定
server.bind((host,port))

# 设置最大连接数
server.listen(5)

while True:
    # 客户端连接
    clientSocket=server.accept()
    address=server.accept()
    print("客户端连接上"+address)
    # 发送消息
    clientSocket.send("你好")
    clientSocket.close()