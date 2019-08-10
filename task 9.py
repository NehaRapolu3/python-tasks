numbers=(1,2,3,4,5,6,7,8,9)
i=0
for x in numbers:
    if x%2==0:
        i=i+1
print("number of even:")
print(i)
j=len(numbers)-i
print("number of odd:")
print(j)
