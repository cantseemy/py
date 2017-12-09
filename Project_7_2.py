#-*- coding:utf-8 -*-
a = input('stroka : ')
b = a.lower().replace(' ','').replace('\'','').replace('\"','')
c = b[::-1]
print(b==c)