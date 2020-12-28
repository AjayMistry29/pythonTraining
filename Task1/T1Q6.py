# 6.Write a program to check the data type of the entered values.
# HINT: Printed output should say -The data type of the input value is : int/float/string/etc

enterd_value = input("Enter something: ")

try:
    if type(eval(enterd_value)) == float:
        print(enterd_value, " is floating point number")
    elif type(eval(enterd_value)) == int:
        print(enterd_value, " is interger number")    
    elif type(eval(enterd_value)) == bool:
        print(enterd_value, " is a boolean")      
except:
    print("That is a string")