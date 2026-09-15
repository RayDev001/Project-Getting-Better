# [HackerRank] - https://hackerrank.com
#
# NOTE: Exercise Python Loops
#
# TODO: The provided code stub reads an integer 'n', from STDIN. For all non-negative integers i < n, print i^2.
#
# WARN: Contraints: 1 <= n <= 20
#
# TEST: -- TEST CASES --
#   - Sample input 0 -> 3
#   - Sample output 0 -> [0,1,4]
#   - Sample input 1 -> 5
#   - Sample output 1 -> [0,1,4,9,16]
#
#
if __name__ == "__main__":
    n = int(input())

    for number in range(n):
        print(number**2)
