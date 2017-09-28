#! /usr/bin/env python3

a = int(input('Введіть число : '))

if ((a&(a - 1)) == 0)==True:
    print('Є степенем 2')
else:
    print('Не є степенем 2')
    
