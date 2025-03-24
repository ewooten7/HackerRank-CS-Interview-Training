# Question 2: Given an integer, n, perform the following conditional actions:
## If n is odd, print Weird
## If n is even and in the inclusive range of 2 to 5, print Not Weird
## If n is even and in the inclusive range of 6 to 20, print Weird
## If n is even and greater than 20, print Not Weird

'Constraints'
## n must be between 1 and 100
## Print Weird if the number is weird. Otherwise, print Not Weird.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

'Essential Questions to Solve: If Else Statements'
# How do I check if a number is odd?
'👉 n % 2 != 0 '

#How do I check if it’s in a range?
'👉 n >= 2 and n <= 5 (or use 2 <= n <= 5 in Python) '

'Plain Step Logic: '
#If n is odd:
#    print "Weird"
#Else:
#    If n is in [2, 5]:
#        print "Not Weird"
#    Else if n is in [6, 20]:
#        print "Weird"
#    Else if n > 20:
#        print "Not Weird"

'Solution'
#!/bin/python3

import math # Math functions like sqrt, pow, ceil, floor, pi
import os # OS operations like file paths, environment vars
import random # Random number generation
import re # Regular expressions for pattern matching
import sys # System-specific parameters (like argv, exit)

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
