# Q2 Swap complex to int variable types and value
complexVar = 20 + 4j
print(type(complexVar))
intVar = 10

complexVar, intVar = intVar, complexVar

print ("Converted Complex:", complexVar)
print ("Converted Int:", intVar)