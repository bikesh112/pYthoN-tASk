#Write a Python program to create the colon of a tuple.
from copy import deepcopy
#create a tuple
tuplex = ("BIKESH", 9, [], True)
print(tuplex)
#make a copy of a tuple using deepcopy() function
tuplex_clone = deepcopy(tuplex)
tuplex_clone[2].append(90)
print(tuplex_clone)
print(tuplex)