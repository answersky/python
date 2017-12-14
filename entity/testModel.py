from entity import test, pythonIo

test.showWord('123')
pythonIo.read('text.txt')
pythonIo.write('text.txt', '123')
try:
    pythonIo.read('text.txt')
except:
    print('文件读取失败')
