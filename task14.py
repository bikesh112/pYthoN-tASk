#Write a Python script to check if a given key already exists in a dictionary.

Adict = {'Mon':3,'Tue':5,'Wed':6,'Thu':9}
print("The given dictionary : ",Adict)
check_key = "Tue"
if check_key in Adict:
   print(check_key,"is Present.")
else:
   print(check_key, " is not Present.")