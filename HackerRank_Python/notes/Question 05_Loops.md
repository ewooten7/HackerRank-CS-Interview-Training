🧠 HackerRank Practice: Print Squares of Non-Negative Integers Less Than n

## ✅ Task
Given an integer n, print the square (i^2) of each non-negative integer i such that:

0 ≤ i < n

Each result should be printed on a new line.

## 📥 Input Format:
A single integer, n.

## 📌 Constraints
1 ≤ n ≤ 20

## 🖨️ Output Format
Print n lines.
Each line should contain the square of the number i (i.e., i * i).

## 🧪 Sample Input
5

## 🧾 Sample Output
0
1
4
9
16

## 🧠 Pseudocode
1. Read integer input `n`
2. Loop from 0 up to (but not including) n
3. For each value of i, print i squared

## 🔍 Key Concepts
range(n):	Generates numbers from 0 to n-1
i ** 2:	    Square of i (i multiplied by itself)
print():	Used to output each result on a new line


## 🧑‍💻 Final Python Code

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)

## 🧠 Interview Tip
This question tests basic loop control, range logic, and mathematical operations in Python.

Pay attention to the exclusive upper bound of range(n) — it will not include n.


`Sample Live Coding Dialogue` 

Interviewer:🎤 Live Coding Dialogue for: “Print the square of all numbers less than n”

💬 "Alright, let me walk you through how I’m thinking about this problem..."

🧠 "So first, I’m being asked to take in a single integer input, n, and then print the square of every non-negative number less than n. That means starting from 0 up to n-1."

🧠 "For example, if n = 5, I should output 0, 1, 4, 9, 16 — that’s 0² through 4². Got it."

🧠 "So I’ll start by reading input from the user — since the code stub provides that, I’ll use n = int(input())."

💡 "Now I want to loop from 0 to n - 1, so I’ll use `range(n)` for that. `Python’s range(n) includes 0 but excludes n, which is perfect.` "

💬 "Inside the loop, I’ll square the current value of i using `i ** 2` , and then print that value."

🧪 "This should result in each square being printed on its own line, which matches the output format."

## Final Code (Live-Typed)
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i ** 2)

🧠 "And that should do it. It handles the constraints of 1 ≤ n ≤ 20, since the logic doesn’t change no matter what n is in that range."

💬 "Let me know if you’d like me to add edge-case checking or error handling, but for this basic task and constraints, I’d consider it complete."

`Terminology Recap`
## if __name__ == '__main__': 
- conditional construct: determines whether a Python script is being run as the main program or if it's being imported as a module into another script. 

- When a Python file is executed directly, the special variable __name__ is set to the string '__main__'. Conversely, when a Python file is imported as a module, __name__ is set to the name of the module.

- Therefore, the code block within the if __name__ == '__main__': statement will only be executed when the script is run directly. This allows for code that should only be run when the script is the main program to be separated from code that defines functions or classes intended for use by other modules.

***
***

## ✅ When should I use if __name__ == '__main__':?

`📌 What it does (in plain English):`
This line tells Python:
👉 “Only run the code inside this block if this file is being executed directly — NOT if it's being imported by another file.”

`🧠 When to use it:`
✅ You're writing a script meant to be run directly
- Example: You want to test something or run a program from the command line.

✅ You have function or class definitions above that you don’t want to run immediately unless the script is executed directly.
- Keeps your reusable code separate from your runtime logic.

✅ You want to keep code modular
- Other files can import functions from your script without accidentally running the entire program.

`🚫 When NOT to use it:`
❌ If you’re writing a quick one-off script that won’t be imported elsewhere.

❌ If you’re running everything in an interactive notebook (like Jupyter).

`Example Use case`
def add(a, b):
    return a + b

if __name__ == '__main__':
    ## This block only runs if the script is executed directly
    print(add(2, 3))

- If this file were imported into another Python file `(import my_script)` , the add() function would still be available, but the print(add(2, 3)) line would NOT execute.

`🔑 Easy Rule of Thumb:`
✅ Use if __name__ == '__main__': if your file:

1) Contains reusable functions and

2) You also want it to behave like a program when run directly.

***
***

## ✅ When to Use for i in range(n)
🔢 You need to `loop a fixed number of times` based on an integer input (n)
- Example: "Print something for each number less than n"

🧮 You need to `generate or manipulate a sequence of numbers` from 0 to n-1
- Example: "Print the square of each number less than n"

🔁 You’re `iterating over a known range of values`, NOT a `list or string`
- Example: "Repeat this block of code for every i from 0 up to (but not including) n"

🚫 You `don’t need to store the values` in a list—just iterate over them
- range(n) is memory efficient and fast for this kind of task.

✅ You want `predictable, incrementing behavior` (starts at 0, goes up by 1)
- Unlike a while loop, a for i in range(n) is cleaner when the number of iterations is known ahead of time.

🤓 Summary:
Use for i in range(n) when you need to perform a task n times, especially if you’re working with index-like values starting from 0.