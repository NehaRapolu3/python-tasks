def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result 


lst = [] 
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
	ele = int(input()) 

	lst.append(ele) # adding the element 
print(multiplyList(lst)) 

