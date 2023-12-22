a=int(input("ENTER THE NUMBER: "))
#a is the variable to match
match a:
# if a is 0
  case 0:
   print("a is zero")
  case 4:
   print("case is 4")
  case _ if a!=90:
   print(a,"is not 90")
  case _ if a!=80:
   print(a,"is not 80")
  case _ :
   print(a)