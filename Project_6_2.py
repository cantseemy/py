#! /usr/bin/env python3

def finalsum(a, b,c):
	fsum = start_sum*((1+percent/100)**year)
	return int(fsum)

start_sum = int(input("Наявна сумма : "))
percent = int(input("Річна процентна ставка : "))
year = int(input("Тривалість депозиту в роках : "))


print(finalsum(start_sum,percent,year))