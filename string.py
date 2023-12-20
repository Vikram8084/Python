# string can be written in the double quote,single quote
name="Vikram"
#multile line string can be written """" __""""/'''__'''
intro='''Hey 
this is vikram
I am student of
Computer Science'''
print(name)
print(intro) 
#to find the length of string we can use len()
l1=len(name)
l2=len(intro)
print("The length of string in name",l1,name)
print("The length of string in intro",l2)
#string slicing
print(name[0:6])
for i in name:
    print(i)