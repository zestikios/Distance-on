import math
from math import radians,asin
p1=float(input('Γεωγρ. πλάτος σημείου Α:'))
m1=float(input('Γεωγρ. μήκος σημείου Α:'))
p2=float(input('Γεωγρ. πλάτος σημείου Β:'))
m2=float(input('Γεωγρ. μήκος σημείου Β:'))
dp=math.radians(p2-p1)
dm=math.radians(m2-m1)
a=math.sin(dp/2)*math.sin(dp/2)+math.cos(math.radians(p1))*math.cos(math.radians(p2))*math.sin(dm/2)*math.sin(dm/2)
c=2*asin(math.sqrt(a))
dist=6372.8*c
print("Η απόσταση τους σε χλμ είναι:",dist)
