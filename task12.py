#Write a Python program to update list element in a set.
#Sample: number = {1,2,3,4,5}
#Output: {1,2,3,4,5,7,8}
num1 = [1,2,3,4,5]
num2 = [7,8] 
set1 = set(num1)
set2 = set(num2)
 
set1.update(set2)
print(set1)
 


