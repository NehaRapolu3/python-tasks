b=input("enter  the triangle sides seperated by space")
a=b.split()
if a[0]==a[1]:
    if a[1]==a[2]:
        print("equilateral triangle")
    else:
        print("isosceles triangle")
else:
    if a[1]==a[2] or a[0]==a[2]:
        print("isosceles triangle")
    else:
        print("scalene triangle")
        
    
        
    
        
