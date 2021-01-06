list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print("List : ",list)

modified_list = [list[0],list[25],list[27],list[28],list[29]]
print(modified_list)

result_list = []
for i in modified_list:
    i = i*i
    result_list.append(i)

print("Requeted List is : ", result_list)


