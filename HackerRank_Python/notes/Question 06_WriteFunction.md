## Opening Question 6:
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Task:
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format:
Read year, the year to test.

Constraints:
1900 ≤ year ≤ 10^5

Output Format:
The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 0: 1990
Sample Output 0: False
Explanation 0: 1990 is not a multiple of 4 hence it's not a leap year.

## Breakdown of Question:
🔍 Understand the Problem
You're asked to implement a function:

def is_leap(year):
    # return True or False

It will return True if the input year is a leap year, otherwise return False.

## 📚 Leap Year Logic
From the prompt:

✅ If a year is divisible by 4, it might be a leap year

🚫 BUT if it's also divisible by 100, it's NOT a leap year

✅ UNLESS it's also divisible by 400 — in that case, it IS a leap year

## 🧠 Pseudocode:
IF (year % 4 == 0)
    IF (year % 100 == 0)
        IF (year % 400 == 0)
            return True
        ELSE
            return False
    ELSE
        return True
ELSE
    return False

## Python Solution:
C

`🎯 How to THINK through this aloud in an interview:` 
“Okay, I know leap years happen every 4 years, but not all years divisible by 4 are leap years. If a year is divisible by 100, it’s normally not a leap year — unless it’s divisible by 400. So I’ll nest some conditionals to reflect this three-part rule. I’ll check if it’s divisible by 4, and if so, handle the exceptions for 100 and 400.”