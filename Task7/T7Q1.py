import math

def square_root(D):
    x = 2 * 50 * D / 30
    return round(math.sqrt(x))

result_list = []
result_list.append(square_root(10))
result_list.append(square_root(20))
result_list.append(square_root(30))

print(result_list)





