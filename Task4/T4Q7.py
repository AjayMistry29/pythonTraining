string1 = input("Enter first string : " )
string2 = input("Enter second string : " )

if len(string1)==len(string2):
    print("String 1 and 2 both has a same length :")
    print("String 1 : ", string1)
    print("String 2 : ", string2)

elif len(string1)>len(string2):
    print("String 1 is longest : ", string1)

else:
    print("String 2 is longest : ", string2)
