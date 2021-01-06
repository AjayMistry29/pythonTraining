numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
target_number = 8

print("Possible Pairs : ")
for i, number in enumerate(numbers[:-1]):  
    complementary = target_number - number
    if complementary in numbers[i+1:]:  
        print((number, complementary))
        