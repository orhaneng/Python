'''
Problem 282 - Project Euler https://projecteuler.net/problem=282
For non-negative integers m, n, the Ackermann function A(m, n) is
defined as follows:

See URL for the formula https://en.wikipedia.org/wiki/Ackermann_function

Find A(1, 0) = 2, A(2, 2) = 7 and A(3, 4) = 125.
'''
def ackermann(input):
    if(len(input)!= 2 ):
        return input
    if input[0]==0 :
        return input[1]+1
    elif input[0] > 0 and input[1] == 0:
        return ackermann(((input[0] - 1),1 ,))
    elif input[0] > 0 and input[1] > 0 :
        return ackermann(((input[0]-1),(ackermann((input[0], (input[1]-1),))),))
    else:
        return input

print(ackermann((1,0,)))
print(ackermann((2,2,)))
print(ackermann((3,4,)))