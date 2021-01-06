even_list=[]
odd_list=[]

while True:
    enter_input = int(input("Enter a number from from 1 to 50: ")) 

    if enter_input>=1 and enter_input<=50 and (enter_input % 2) != 0 and len(odd_list)<5: 
       odd_list.append(enter_input)
       print("Odd List :" ,odd_list) 
       continue
     
   
    elif enter_input>=1 and enter_input<=50 and (enter_input % 2) == 0 and len(even_list)<5:
       even_list.append(enter_input)
       print("Even List :" ,even_list)
    
    
   
    else:
       print("Entered Number is out of range")      
       break
   
   
print("Sum of Even Numbers List is :", sum(even_list))
print("Sum of Odd Numbers List is :", sum(odd_list))
print("Maximum number from Even List is :", max(even_list))
print("Maximum number from Odd List is :", max(odd_list))

           

  

           

         