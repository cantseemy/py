#! /usr/bin/env python3

import math
from decimal import Decimal

a = float(input("Зарплата працівника : "))

b = Decimal((a*18)/100)
c = Decimal((a*1.5)/100)
d = Decimal(b) + Decimal(c)
e = Decimal(a) - Decimal(d)

print("Зарплата  : ",a,"|", "Податок : ",d,"|","Після оплати податку",e)


