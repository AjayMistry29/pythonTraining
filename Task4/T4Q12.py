def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Sorry!! You can not divide any number by zero")
except:
    print("Any other exception")