🧠 HackerRank Practice: Integer & Float Division
📝 Problem Summary
You're given two integers, a and b. You need to:

Print the result of integer division a // b

Print the result of float division a / b

No rounding or formatting is needed.

Input Format:
The first line contains the first integer, a.  
The second line contains the second integer, b.

🖨️ Output Format
The first line contains the result of a // b (integer division).  
The second line contains the result of a / b (float division).

🧠 Pseudo Code
1. Read two integers a and b from user input
2. Perform integer division using //
3. Perform float division using /
4. Print both results on separate lines

Sample Input:
4
3

Sample Output:
1
1.3333333333333333

💡 Key Concepts
Operator	Description	            Example (a = 4, b = 3)
//	        Integer division (truncates)	4 // 3 = 1
/	        Float division (precise value)	4 / 3 = 1.333...

# Solution 
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)  # Integer division
    print(a / b)   # Float division


⚠️ Notes
// returns the quotient without decimals

/ returns a float result

Python’s default division with / retains full precision—no rounding needed unless specified