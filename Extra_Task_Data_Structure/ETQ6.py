def printWords(s): 
        
    s = s.split(' ')  
       
    for word in s:  
          
        if len(word)%2==0: 
            print(word)  

s = "hello my name is abcde" 
printWords(s) 