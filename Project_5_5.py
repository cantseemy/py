#! /usr/bin/env python3

a = int(input("Введіть число : "))
i=0
s=0
while i<=a:
	i=i+1
	if a%i==0:
		s=s+1
if s <= 2:
	print("Число просте ")
if s > 2:
	print("Число складене ")
	
