def generate_fibonacci_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [fibonacci(j) for j in range(i + 1)]
        triangle.append(row)
    return triangle

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))  # List into String conversion


rows = 5
fibonacci_triangle = generate_fibonacci_triangle(rows)
print_fibonacci_triangle(fibonacci_triangle)


"""
READ IT
Step:1 --> Enter the value 5
Step:2 --> generate_fibonacci_triangle(5)
           for 0 - 5
               row -> for 0 - 1                                             # for j in range(i + 1)
                   fibonacci(0) -> return 0                                 --> [0]
           for 1 - 5
               row -> for 0 - 2                                             # for j in range(i + 1)
                   fibonacci(0) -> return 0
                   fibonacci(1) -> return 1                                 --> [0,1]
            for 2 - 5
               row -> for 0 - 3                                             # for j in range(i + 1)
                   fibonacci(0) -> return 0
                   fibonacci(1) -> return 1
                   fibonacci(2) -> return fibonacci(2-1) + fibonacci(2-2)
                                               |                 |
                                          return 1     +     return 0       --> [0,1,1]
            for 3 - 5
               row -> for 0 - 4                                             # for j in range(i + 1)
                   fibonacci(0) -> return 0
                   fibonacci(1) -> return 1
                   fibonacci(2) -> return fibonacci(2-1) + fibonacci(2-2)
                                               |                 |
                                          return 1     +     return 0       --> return 1
                   fibonacci(3) -> return fibonacci(3-1) + fibonacci(3-2)
                                               |                 |
                                          fibonacci(2)      + fibonacci(1)     
                                               |                    | 
                                   fibonacci(2-1) + fibonacci(2-2)  |
                                          |               |         | 
                                       return 1   +  return 0  +  return 1   --> [0,1,1,2]
"""
