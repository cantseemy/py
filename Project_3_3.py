#! /usr/bin/env python3

"""
Сметана Тарас Васильович
"""

weight = input('Ваша вага : ')
height = input('Ваш зріст : ')

height = float(height)
weight = float(weight)

BMI = (weight/height**2)
print('Індекс Маси Тіла : ', BMI)



