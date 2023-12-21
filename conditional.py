a=int(input("Enter the marks of Physics: "))
b=int(input("Enter the marks of Chemistry: "))
c=int(input("Enter the marks of Mathematics: "))
d=int(input("Enter the marks of English: "))
e=int(input("Enter the marks of IT: "))
avg=(a+b+c+d+e)/5
print("The average of marks: ",avg)
if(avg>65):
  print("You passed exam with first Divison",avg)
elif( 35 < avg < 65):
  print("You passed exam with 2nd Divison",avg)
else:
  print("you passed with 3rd Divison",avg)
    