
def function1(x):
    return x**2

def function2(x):
    return function1(x) + x * 5

if __name__ == '__main__':
    print(function1(5))
    print(function2(5))