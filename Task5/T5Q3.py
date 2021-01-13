user_input = input("Enter a number:")
z = len(user_input)
try:
    if z>4:
        raise ValueError("Length is too long. Please Provide only four digits.")
    if z<4:
        raise ValueError("Length is too short. Please provide only four digits.")
    if z==4:
        raise ValueError("Length is perfect. Thank you.")
    
except ValueError as ve:
    print(ve)
