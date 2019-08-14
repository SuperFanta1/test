'''
@Author: yasuo
@Date: 2019-08-14 14:19:12
@LastEditors: yasuo
@LastEditTime: 2019-08-14 14:25:42
'''
#打印杨辉三角
def triangles(n):
    yield [1]
    yield [1,1]
    last = [1,1]
    while True:
        t = tuple(last)
        n = 1
        while n < len(t):
            last[n] = t [n] + t[n-1]
            n = n+1
        last.append(1)
        yield last[:]

if __name__ == '__main__':
    a = triangles(5)
    for i in a:
        print(i)