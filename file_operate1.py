import os

#打印当前工作目录
pwd = os.getcwd()
#切换到目录“目录”
#os.chdir("目录")
print("当前工作目录为：",pwd)

#打印当前文件夹下文件列表
dir_list = os.listdir()
print("当前目录下文件列表：",dir_list)

#更改文件名:将 bili01.txt 修改为 bili01.py
print("旧文件名为",dir_list[1])# bili01.txt
# new_name = os.rename(bili01.txt,bili01.py)
# print("当前目录下文件列表：",dir_list)\

#检查当前目录下是否存在 file_test1.txt 若不存在则创建
try:
    file_name1 = "file_test1.txt"
    f = open(file_name1)
except FileNotFoundError:
    print("文件不存在！将会自动创建。。。")
    os.system(r"touch {}".format(file_name1))
print("当前目录下文件列表：",os.listdir())
