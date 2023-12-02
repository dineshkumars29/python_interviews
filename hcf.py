"""

READ IT
Step 1 -> if number2 bigger then number1 just swap it
Step 2 -> Loop will execute till while condition satisfied
Step 3 -> number1 = 48 , number2 = 18
          1st loop
               temp = number2 => 18
               number2 = 48 % 18 => 12
               number1 = 18
          2nd loop
               temp = number2 => 12
               number2 = 18 % 12 => 6
               number1 = 12
          3rd loop
               temp - number2 => 6
               number2 = 12 % 6 => 0
               number1 = 6
          number2 = 0 Here while condition satisfied so loop return number1 value 6

"""


def two_number(num_1, num_2):
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    while num_2 != 0:
        temp = num_2
        num_2 = num_1 % num_2
        num_1 = temp
        print(num_1)
        print(num_2)
    return num_1


def func(number_1, number_2):
    temp = number_1 % number_2
    return temp


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

hcfValues = two_number(num1, num2)

print(f"your {num1},{num2} two numbers hcf is {hcfValues}")
