##
#2 empty bottle exchange a bottle, 5 shell exchange a bottle
##
import math
empty=1000
shell = 1000
number = 1000
def num(empty,shell):
    return math.floor(empty/2)+math.floor(shell/4)

while empty>=2 or shell>=4:
    delta = num(empty,shell)
    empty=empty%2+delta
    shell=shell%4+delta
    number+= delta
    
print(number)    
