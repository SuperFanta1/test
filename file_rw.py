'''
@Author: yasuo
@Date: 2019-08-13 20:46:29
@LastEditors: yasuo
@LastEditTime: 2019-08-14 09:05:49
'''
#文件的读写操作
import sys

file_obj = open("file_test1.txt","r+")

print("文件名：{}"'\n'"是否已关闭：{}"'\n'"访问模式：{}".format(file_obj.name,file_obj.closed,file_obj.mode))

#写入数据
#data = input("请输入数据：")
#多行输入

datas = []
while True:
    try:
        datas.append(input("请输入数据："))
    except:
        break

for data in datas:
    file_obj.writelines(data)
file_obj.close

