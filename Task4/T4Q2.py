def upperlower(string): 
  
    upper = 0
    lower = 0
  
    for i in string: 
        if (i>='a'and i<='z'): 
            lower=lower+1  

        if (i>='A'and i<='Z'): 
            upper=upper+1 
  
    print('Lower case characters = %s' %lower, 
          'Upper case characters = %s' %upper) 
  
string = input("Enter the String :")
upperlower(string) 