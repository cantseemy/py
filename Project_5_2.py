#! /usr/bin/env python3

print('''
  #########
 #       ##
#       # #
########  #
#      # #
#      ## 
########
''')

print("""
#door
""")
h = float(input('Висота дверей : '))
w = float(input('Ширина дверей : '))
print("""
#box
""")
a = float(input('Висота коробки : '))
b = float(input('Ширина коробки : '))
c = float(input('Довжина коробки : '))

if ((h>=a) and (w>=b)) or ((h>=c) and (w>=b)) or ((h>=a) and (w>=c)) or ((w>=a) and (h>=b)) or ((w>=c) and (h>=b)) or ((w>=a) and (a>=c)): 
    print('Коробка поміщається')
else:
    print('Коробка не поміщається')

