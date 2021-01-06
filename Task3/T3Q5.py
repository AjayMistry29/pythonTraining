list = [3,5,5,34,65,4,67,4,6,31]
print("List : ",list)

requested_list = []

for i in list:
    if i % 2 != 0:
        requested_list.append(i)  

print("New List without even numbers is : ", requested_list)