#! /usr/bin/env python3

import random
print('''
#1 - ножниці 
#2 - папір 
#3 - камінь 
''')

print('--------')

step = int(input('Ваш хід  : '))

if step >=4:
	while step >=4:
		print('''
#1 - ножниці 
#2 - папір 
#3 - камінь 
		''')
		step = int(input('Ваш хід  : '))
		if step >=4:
			continue
		else:
			break


comStep = random.randint(1,3)

print('--------')

print("Компуктер ставить: ",comStep)
print('--------')

if step == comStep:
	print("Нічия")
elif step == 1 and comStep == 2:
	print("Ви перемогли!")
elif step == 2 and comStep == 3:
	print("Ви перемогли!")
elif step == 1 and comStep == 3:
	print("Переміг компуктер")
elif step == 2 and comStep == 1:
	print("Переміг компуктер")
elif step == 3 and comStep == 1:
	print("Ви перемогли!")
elif step == 3 and comStep == 2:
	print("Переміг компуктер")




