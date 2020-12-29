number = int(input("Guess the lucky number from 1 to 10 : " ))
while True: 
            if number != 5:
                          print("That is not your luckey number, Sorry!!")
                          user_Input = input("Want to guess more? Please type Yes or No :" )
                          if user_Input == "No":
                               print("Sorry!! You loose.")
                               break
                            
                          number = int(input("Guess the lucky number from 1 to 10 :" ))
                          continue
                              
                 
            else:
                  print ("Yay!! That is your lucky number") 
                  break 
             
     

