s = input("Please enter a string :" )

letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)

print("Letters ", letters)
print("Digits " ,digits)