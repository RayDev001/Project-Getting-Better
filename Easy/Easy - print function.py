# [HackerRank] - https://hackerrank.com
#
# NOTE: Exercise Python Print Function
#
# TODO: The provided code stub reads an integer 'n', from STDIN.
# Without using any string methods, try to print the following: 123... n.
# Note that "..." represents the consecutive values in between.
#
# WARN: Contraints: 1 <= n <= 150
#
# TEST: -- TEST CASES --
#   - Sample input 0 -> 3
#   - Sample output 0 -> 123
#   - Sample input 1 -> 5
#   - Sample output 1 -> 12345
#
#
if __name__ == "__main__":
    n = int(input())

    output = ""
    for i in range(1, n + 1):
        output += str(i)

    print(output)
