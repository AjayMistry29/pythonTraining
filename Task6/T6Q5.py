def f1(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@f1
def f2():
    print("f2")

f2()

