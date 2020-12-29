
num1 = int(input ("Choose your first number: "))
num2 = int(input ("Choose your Second number: "))

opration = input("Select any one from following options 1.Add 2.Sub 3.Div 4.Mul 5.Avg : " )

if num1 or num2 < 0:
    print("Negative")

elif opration == "Add":
     add = num1 + num2
     print("Addition of two number is: " , add)

elif opration == "Sub":
     sub = num1 - num2
     print("Subtraction of two number is: " , sub)

elif opration == "Div":
     div = num1 / num2
     print("Division of two number is: " , div)

elif opration == "Mul":
     mul = num1 * num2
     print("Multiplication of two number is: " , mul)

elif opration == "Avg":
     avg = (num1 * num2) / 2
     print("Avarage of two number is: " , avg)

else:
   print("Negative number")

