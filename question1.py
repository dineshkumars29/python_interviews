"""
convert "a2b2c3d4" -> "aabbcccdddd"
"""
str_1 = ""
str_2 = ""
def func(value):
    global str_2
    for i in range(0,len(value),2):
        num_1 = int(value[i+1])
        str_1 = num_1 * value[i]
        str_2 += str_1
    return str_2

str_Value = "a2b2c3d4"
result = func(str_Value)
print(result)