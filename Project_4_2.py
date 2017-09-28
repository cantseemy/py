#! /usr/bin/env python3

import math

a = float(input("Введіть змінну а : "))
b = float(input("Введіть змінну b : "))
c = float(input("Введіть змінну c : "))

'''
d = ((1)/(c*math.sqrt(2*math.pi)))

e = ((a-b)**2)*(-1)

g = (2*c)**2

h = math.exp(e/g)

print(d*h)
'''

print(((1)/(c*math.sqrt(2*math.pi)))*(math.exp((((a-b)**2)*(-1))/((2*c)**2))))
