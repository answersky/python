def read(file_path):
    file = open(file_path, 'r')
    str = file.read()
    print(str)
    file.close()


def write(file_path, string):
    file = open(file_path, 'a')
    file.write(string)
    file.close()

