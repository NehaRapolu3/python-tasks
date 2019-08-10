filename=input('enter filename')
index=0
for i in range(len(filename)):
    if filename[i]=='.' :
        index=i
print(filename[index+1:])        
    

