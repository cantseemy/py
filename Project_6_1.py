#! /usr/bin/env python3

import math

def area(a, b, c):
	Pr = a + b + c
	p = Pr/2
	d = (p*(p-a)*(p-b)*(p-c))
	s = math.sqrt(d)
	return s

fside = int(input("Перша сторона трикутника : "))
if fside <= 0 :
	while fside <= 0:
		fside = int(input("Перша сторона трикутника : "))
		continue
sside = int(input("Друга сторона трикутника : "))
if sside <= 0 :
	while sside <= 0:
		sside = int(input("Друга сторона трикутника : "))
		continue
tside = int(input("Третя сторона трикутника : "))
if tside <= 0 :
	while tside <= 0:
		tside = int(input("Третя сторона трикутника : "))
		continue

if fside > sside + tside:
	print("Сорі але трикутник не існує")
elif sside > fside + tside:
	print("Сорі але трикутник не існує")
elif tside > fside + sside:
	print("Сорі але трикутник не існує")
else:
	print(area(fside, sside,tside))
