#! /usr/bin/env python3

def need_year(start_sum, need_sum, percent):
	year = 0
	while start_sum < need_sum:
		start_sum = start_sum + start_sum * (percent/100)
		year = year + 1
	return year

start_sum = int(input("Наявна сумма : "))
need_sum = int(input("Потрібна сумма : "))
percent = int(input("Річна процентна ставка : "))

print("Потрібно років : ",need_year(start_sum, need_sum, percent))
