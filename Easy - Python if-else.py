# [HackerRank] - https://hackerrank.com
#
# NOTE: Exercise Python If-Else
#
# TODO: Given an integer 'n', perform the following conditional actions:
#   - if 'n' is odd, print "Weird"
#   - if 'n' is even and in the inclusive range of 2 to 5, print "Not Weird"
#   - if 'n' is even and in the inclusive range of 6 to 20, print "Weird"
#   - if 'n' is even and greater than 20, print "Not Weird"
#
# WARN: Contraints: 1 <= n <= 100
#
# TEST: -- TEST CASES --
#   - Sample input 0 -> 3
#   - Sample output 0 -> Weird
#   - Sample input 1 -> 24
#   - Sample output 1 -> Not Weird
#
def isWeird(n: int) -> None:
    if n % 2 == 0:
        # NOTE: added 1 because the range functions is not inclusive by default. Meaning, include need to incremenet the top range by 1 to include the last number
        if n in range(2, 5 + 1):
            print("Not Weird")
        elif n in range(6, 20 + 1):
            print("Weeird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")


n = int(input("Type the number: ").strip())

isWeird(n)
