
#how to call the function form one module to onther module
#Appraoch 1
# import claculator
# claculator.mul(11,22) #every time calling using class then method
# claculator.add(11,22)

#Appraoch 2
# from claculator import add,mul
# mul(11,22)  #but you have too much method then like (add,mul) import all
# add(11,22)

#Appraoch 1
from claculator import *
mul(11,22) #using * no need to call every method
add(11,22)