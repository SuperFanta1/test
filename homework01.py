# coding=utf-8
"""
作业：
定义一个函数，参数为列表（数据项为int），返回这个列表中的最大值和最小值。
"""
import random

#random.sample() 生成互不相同的随机数
#range(start,stop,step) 不包括结束值
ls = random.sample(range(1,50),20)
print(ls)

#方法一：
#打印列表中最大值
def print_max1(item):
    the_max = item[0]
    for i in range(1,20):
        if item[i]>the_max:
            the_max = item[i]
            i = i+1
        else:
            the_max = the_max
    print("列表中最大值是：{}".format(the_max))
print_max1(ls)

#打印列表中的最小值
def print_min1(item):
    the_min = item[0]
    for i in range(1,20):
        if item[i]<the_min:
            the_min = item[i]
            i = i+1
        else:
            the_min = the_min
    print("列表中最小值是：{}".format(the_min))

print_min1(ls)

#方法二：对方法一的简化
def print_max2(items):
    the_max = items[0]
    for item in items:
        if item > the_max:
            the_max = item
    print("列表最大值：",the_max)

def print_min2(items):
    the_min =items[0]
    for item in items:
        if item < the_min:
            the_min = item
    print("列表最小值：",the_min)

print_max2(ls)
print_min2(ls)

#方法三：sort()函数
#sort() 正序从小到大排序
def print_max_and_min(items):
    items.sort()
    the_max = items[len(items)-1]
    the_min = items[0]
    print("列表最大值是：{}\n列表最小值是：{}".format(the_max,the_min))
print_max_and_min(ls)