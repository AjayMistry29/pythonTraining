students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

# Method-1(Using zip function only)
# x = zip(students,subjects)
# print(dict(x))

# Method-2 (Dictionary Comprehensive for loop and zip function)
x = {k:v for (k,v) in zip(students,subjects)}
print(x)