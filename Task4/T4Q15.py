def mul(n):
    return n*n

numbers = (1,2,3,4,5)
result = map(mul, numbers)
print(list(result))