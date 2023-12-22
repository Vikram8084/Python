import time
timestamp=time.strftime('%H : %M : %S')
print(timestamp)
a=int(time.strftime('%H'))
print(a,"Hours")
b=int(time.strftime('%M'))
print(b,"Minutes")
c=int(time.strftime('%S'))
print(c,"Seconds")
if(6 < a <12 and 1 < b <59 and 1 < c <59):
    print("GOOD MORNING")
elif(12 < a <17 and 1 < b <59 and 1 < c <59):
    print("GOOD AFTERNOON")    
elif(17 < a <20 and 1 < b <59 and 1 < c <59):
    print("GOOD EVENING")    
else:
    print("GOOD NIGHT")