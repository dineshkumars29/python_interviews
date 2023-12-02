# double one triple two double five six double four

input_number = input("Enter your numbers in words:")
print(input_number)
words = input_number.split()
print(words)
newWords = []
a = ""
for i in range(len(words)):
    if words[i] == "double":
        newWords.append(words[i + 1])

    elif words[i] == "triple":
        newWords.append(words[i + 1])
        newWords.append(words[i + 1])
    else:
        newWords.append(words[i])
print(newWords, "ddfddfdfdf")


def switch(values):
    global a
    for i in values:
        if i == 'one':
            a = a + "1"
        elif i == 'two':
            a = a + "2"
        elif i == 'three':
            a = a + "3"
        elif i == 'four':
            a = a + "4"
        elif i == 'five':
            a = a + "5"
        elif i == 'six':
            a = a + "6"
        elif i == 'seven':
            a = a + "7"
        elif i == 'eight':
            a = a + "8"
        elif i == 'nine':
            a = a + "9"
    return a


better = switch(newWords)
print(better)
