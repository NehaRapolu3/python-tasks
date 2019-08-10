   
function= input("enter names seperated by space")
words = function.split(" ")
length = 0
word = " "
for i in range(len(words)) :
    if len(words[i]) > length :
        length = len(words[i])
        word = words[i]    
print(word)  
