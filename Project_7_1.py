# -*- coding: utf-8 -*-
word = input('word : ')
while 1:
	try:
		step = int(input('chyslo :'))
		if step > (len(word)/2):
			while step > (len(word)/2):
				step = int(input('chyslo !> len(word):'))
		break
	except ValueError:
			print('chyslo a ne symvol')



def cut(word, step):
	return word[step:] + word[:step]

print(cut(word, step))