## HackerRank Practice: Arithmetic Operators

📝 Problem Summary
You are given two integers a and b.
You need to:

Print their sum
Print their difference (a - b)
Print their product


📥 Input Format
The first line contains the first integer, a.  
The second line contains the second integer, b.

📌 Constraints
1 ≤ a ≤ 10^10  
1 ≤ b ≤ 10^10

🖨️ Output Format
Print the sum on the first line  
Print the difference on the second line  
Print the product on the third line

🧠 Pseudo Code
1. Read two integers a and b from user input
2. Compute the sum (a + b)
3. Compute the difference (a - b)
4. Compute the product (a * b)
5. Print the results in order, each on a new line

🧪 Sample Input
Copy
Edit
3
2

✅ Sample Output
Copy
Edit
5
1
6

🧑‍💻 Python Code Solution
python

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)   # Sum
    print(a - b)   # Difference
    print(a * b)   # Product

🔍 Notes
Python handles large integers well, so no need to worry about 10^10 as long as you’re using int().

Always check the order of operations and format of the output in HackerRank problems.

input() reads input as a string, so we convert to int first.

## Solution

