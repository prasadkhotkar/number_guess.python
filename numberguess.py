import random
userinput=int(input("enter the any number"))
cnumber=random.randrange(1,101)

if cnumber<userinput:
    print("computer number",cnumber)
    print("enterd number is grater than computer number")
elif cnumber>userinput:
    print("computer number",cnumber)
    print("enterd number is less than computer number")

else:
    print("computer number",cnumber)
    print("your number and computer number is equal")        
