

number = int(input("Guess the lucky number from 1 to 10 : " ))
counter = 1
while number !=5:
                    if counter <=4:
    
                          print("That is not your luckey number, Sorry!! Chances left :" , counter)
                          print("Try Again!!")
                          counter = counter + 1
                          number = int(input("Guess the lucky number from 1 to 10 : Chances left!!"))
                          continue
                          
                    else:
                         print("Game Over!")
                         break
                                           
else:
    print ("Correct number is guessed!!") 
    
             
     

