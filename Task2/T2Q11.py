

number = int(input("Guess the lucky number from 1 to 10 : " ))
counter = 1
while number !=5:
                    if counter <=4:
    
                          print("That is not your luckey number, Sorry!! Chances left :" , counter)
                          print("Try Again!!")
                          user_Input = input("Want to guess more? Please type Yes or No :" )
                          if user_Input == "No":
                               print("Sorry!! but that was not very successfull")
                               break
                          counter = counter + 1
                          number = int(input("Guess the lucky number from 1 to 10 : Chances left!!"))
                          continue
                          
                    else:
                         print("Game Over!")
                         break
                                           
else:
    print ("Correct number is guessed!!") 
    
             
     

