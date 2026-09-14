# [HackerRank] - https://hackerrank.com
#
# NOTE: Exercise Python Division
#
# TODO: The provided code stub reads two integers from STDIN, 'a' and 'b'. Add code to print two lines where:
#  1. The first line should contain the result of integer division of the two numbers. => ['a' // 'b']
#  2. The second line should contain the result of float division of the two numbers. => ['a' / 'b']
#
# WARN: Contraints: None
#
# TEST: -- TEST CASES --
# Sample input 1: (a = 3, b = 5)
# sample output 1: (0, 0.6)
# sample input 2: (a = 4, b = 3)
# sample output 2: (1, 1.33333)

if __name__ == "__main__":
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)
