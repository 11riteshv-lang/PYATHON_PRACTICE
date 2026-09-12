# This program takes an integer input from the user and reverses the digits of that number.

n = int(input("Enter a number: "))

y = n

r = 0
while n != 0:
    r = r + (n % 10)
    r = r * 10
    n = n // 10

r = r // 10

x = r + y 

print("The sum of the original number and its reverse is:", x)