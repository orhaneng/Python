'''
(https://projecteuler.net/problem=414)

6174 is a remarkable number; if we sort its digits in increasing order
and subtract that number from the number you get when you sort the digits
in decreasing order, we get 7641-1467=6174. Even more remarkable is that
if we start from any 4 digit number and repeat this process of sorting and
subtracting, we'll eventually end up with 6174 or immediately with 0 if
all digits are equal. This also works with numbers that have less than 4
digits if we pad the number with leading zeroes until we have 4 digits.
E.g. let's start with the number 0837:
8730-0378=8352
8532-2358=6174
6174 is called the Kaprekar constant. The process of sorting and
subtracting and repeating this until either 0 or the Kaprekar constant
is reached is called the Kaprekar routine.
Write a Python program to calculate the number of steps to reach the
Kaprekar constant for values 8730 and 9730.

'''
def question2(digit):
    if not digit or digit == 6174 or digit <= 0:
        return 0
    return question2(
        int(''.join(sorted(str(digit).zfill(4), reverse=True))) - int(''.join(sorted(str(digit).zfill(4))))) + 1

print('number of steps for 1111: ' + str(question2(8730)))
print('number of steps for 9730: ' + str(question2(9730)))



