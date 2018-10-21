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
def question2(digit):
    if not digit or digit == 6174 or digit <= 0:
        return 0
    return question2(
        int(''.join(sorted(str(digit).zfill(4), reverse=True))) - int(''.join(sorted(str(digit).zfill(4))))) + 1

print('number of steps for 1111: ' + str(question2(8730)))
print('number of steps for 9730: ' + str(question2(9730)))



