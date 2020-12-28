# Q5. Write a program to complete the task given below:
#     Ask users to enter any 2 numbers in between 1-10 ,
#     add the two numbers and keep the sum inanother variable called z.
#     Add 30 to z and store the output in variable result and print result as thefinal output.

numFirst = input("Please enter any one number between 1 to 10 :" )
numSecond = input("Please enter second number between 1 to 10 :" )

z = numFirst + numSecond
e = int(z)
result = e + 30
print("The final output:", result)