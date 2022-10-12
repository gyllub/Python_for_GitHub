# The Fibonacci sequence is one of the most famous formulas in mathematics.
# Each number in the sequence is the sum of the two numbers that precede it.
# For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.
#
# Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).
#
# Sample Input
# 6
#
# Sample Output
# 0
# 1
# 1
# 2
# 3
# 5
# If you are making the Fibonacci sequence for n

def fibonacci (loop_count ):
    pred=0
    nast=1
    print(0)
    print (1)
    for i in range (2,loop_count ):
        nast, pred=nast+pred, nast
        print(nast)


loop_count  = int(input())



if loop_count == 1:
    print (0)
elif loop_count ==2:
    print (0)
    print (1)
else:fibonacci(loop_count)