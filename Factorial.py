# Factorial -> 5! => 120

a = 1


def func(value):
    global a
    for i in range(1, value + 1):
        a *= i
    return a


number = int(input("Enter your number here: "))

factorial = func(number)
print(factorial)
