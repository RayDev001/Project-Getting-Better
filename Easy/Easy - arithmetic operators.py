# [HackerRank] - https://hackerrank.com
#
# NOTE: Exercise Python Arithmetic Operators
#
# TODO: The provided code stud reads two integers from STDIN, 'a' and 'b'. Add code to print three lines where:
#  1. The first line contains the sum of the two numbers.
#  2. The second line contains the difference of the two numbers (first - second)
#  3. The third line contains the product of the two numbers
#
# WARN: Contraints: 1 <= a <= 10^10 and 1 <= b <= 10^10
#
# TEST: -- TEST CASES --
# Sample input 1: (a = 3, b = 5)
# sample output 1: (8, -2, 15)
# sample input 2: (a = 3, b = 2)
# sample output 2: (5, 1, 6)

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)
