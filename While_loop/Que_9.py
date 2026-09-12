# This program calculates the factorial of a given number using a for loop.

n = int(input("Enter a number: "))

count = 1

for i in range(1, n+1, 1):      # yaha pe mene sidha loop chalay hai.
    count = count * i
    print("The factorial of", n, "is", count)