import math 
import random

lst=[16,2.7,25,-3.4,9,1.5,36,4.8]

val= random.choice(lst)

rem = math.trunc(val)

roots = []

if val == rem:
    scuare = math.sqrt(val)
    roots.append(scuare) 
    
rounded = []

for i in enumerate(lst):
    if i % 2 == 0:
        rounded.append
    