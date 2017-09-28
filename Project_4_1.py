#! /usr/bin/env python3

import math

a = float(input("Введіть змінну а : "))
b = float(input("Введіть змінну b, b ≠ 0 : "))
 
if b == 0:
	while b == 0:
		b = int(input("Введіть змінну b, b ≠ 0 : "))
		if b == 0:
			continue
		else:
			print("Результат формули : ", (math.sqrt(a*b))/(math.exp(a)*b)+(a*math.exp(((2*a)/b))))
else:
	print("Результат формули : ", (math.sqrt(a*b))/(math.exp(a)*b)+(a*math.exp(((2*a)/b))))

