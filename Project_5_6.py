#! /usr/bin/env python3

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

if fside +sside >tside:
	print("Існує")
elif fside + tside >sside:
	print("Існує")
elif sside + tside > fside:
	print("Існує")
else:
	print("Не існує")

