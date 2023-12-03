# generate Fibonacci
"""

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones,
usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
The mathematical formula for the Fibonacci sequence is often given as:

F(n)=F(n−1)+F(n−2)

with initial conditions
F(0)=0 and F(1)=1.

This sequence is named after Leonardo Fibonacci, an Italian mathematician who introduced it to the Western world
 in his 1202 book "Liber Abaci."

IN PYTHON
fib_sequence[-1] refers to the last element in the list.
fib_sequence[-2] refers to the second-to-last element in the list.

"""


def fib_func(value):
    global inicial
    fib_inicial = [0, 1]

    while len(fib_inicial) < value:
        inicial = fib_inicial[-1] + fib_inicial[-2]
        fib_inicial.append(inicial)
    return fib_inicial


number = int(input("Enter your number here: "))
inicial = 0

gen = fib_func(number)

print(gen)
