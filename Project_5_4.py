#! /usr/bin/env python3

import math

print("a * x^2 + b * x + c = 0 ")

a = int(input("a = "))
if a == 0:
	while a == 0:
		a = int(input("a = "))
		continue

b = int(input("b = "))
c = int(input("c = "))

d = b**2-4*a*c

if d == 0:
	x = -1*b/2*a
	print("D = 0, Коренем рівняня є : ",x)
elif d < 0:
	print("D < 0, Коренів немає")
else:
	x1 = (-1*b+math.sqrt(d))/(2*a)
	x2 = (-1*b-math.sqrt(d))/(2*a)
	print("D > 0, Корені рівняння : ","x1 = ",x1,"|","x2 = ",x2)
