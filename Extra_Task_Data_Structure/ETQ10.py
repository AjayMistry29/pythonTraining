tuple1 = (1,2,3,4,5,6,7,8,9,10)
list = []
for i in tuple1:
    if i % 2 == 0:
        list.append((i))
        
def convert(list): 
    return tuple(list) 
  
# Driver function 
print("Even Tuple: " , convert(list)) 