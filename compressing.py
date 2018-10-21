'''
https://en.wikipedia.org/wiki/Run-length_encoding
Implement an encoding scheme.
A string
WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
has 67 characters. Write a Python program to convert this string to
12W1B12W3B24W1B14W. The new string is created
by calculating the number of times a characters appears consecutively and
placing the character next to it. The new string only needs 18 character,
thus compressing the original string by 73%.

'''
# OMER ORHAN
def question1(text):
    flag = ''
    count = 0
    result = ''
    if not text:
        return ''
    for index in range(0, len(text)):
        if text[index] != flag and flag:
            result = result + str(count) + flag
            flag = text[index]
            count = 0
        elif index == len(text) - 1:
            result = result + str(count + 1) + flag
            break
        if flag == '':
            flag = text[index]
        count = count + 1
    return result

text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(question1(text))


