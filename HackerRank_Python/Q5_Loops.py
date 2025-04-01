if __name__ == '__main__': 
    n = int(input("Enter a number between 1 and 20: "))

    #Check
    if 1 <= n <= 20:
        for i in range(n):
            print(i ** 2)
    else:
        print("Error: Input must be between 1 and 20")