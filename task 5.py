r=input("enter the month")
a=("January","March","May","July","August","October","December")
b=("February")
if r in a:
    print("The month has 31 days ")
elif r in b:
    print("The month has 28 days")
else:
    print("The month has 30 days")
