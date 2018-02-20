# Question 1
# Level 1
#
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method


    def div():
        for x in range(2000, 3200):
            print(x)
            if x % 7 == 0 and not x % 5 == 0:
                return print(x)

            else:
                return False