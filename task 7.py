a=input("enter three values seperated by space:")
b=a.split(" ")
if b[1]<b[2]:
    if b[2]<b[0]:
        print("median is "+ b[2])
    elif b[0]>b[1]:
        print("median is "+ b[0])
    else:
        print("median is "+ b[1])
else:
    if b[1]<b[0]:
        print("median is "+ b[1])
    elif b[0]>b[2]:
        print("median is "+ b[0])
    else:
        print("median is "+ b[2])
    
    
        
