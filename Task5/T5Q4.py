
print('Enter username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Ajay2904':
        print('Access granted')
        break
    else:
        print('Access denied.')
        count += 1

