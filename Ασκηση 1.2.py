
x=int(input(' Όρισε έναν ακέραιο x:'))
y=int(input(' Όρισε έναν ακέραιο y:'))
import math
print('{:^10.3f}{:^10d}{:^10.3f}{:^10.3f}{:^10.3f}'.format(x/y,x%y,math.log(x,y),math.sqrt(y),math.exp(x)))
