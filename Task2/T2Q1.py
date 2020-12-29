# T2Q2 Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as astring.

x = input("Write any number :" )

number = int(x)

if number == 0:
    print ("Zero is not div, Try something else")

elif number % 3 == 0 and number % 5 == 0:
    print ("Consultadd - Python Traning")

elif  number % 3 == 0:
    print ("Consultadd")

elif number % 5 == 0:
    print("Python Training")

else :
    print("Try something else")


