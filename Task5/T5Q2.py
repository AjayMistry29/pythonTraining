while True:
    try:
        user_input = input("Enter the file name: ")
        f = open(user_input)   
    except:
         print("File does not exist. Try again!!")      
    else:
        print("File is traced sucessfully!!")
        break


