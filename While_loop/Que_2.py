
n = int(input("Enter a number: "))

a = 0

while n != 0:
    n = n // 10
    a = a + 1

print("The number of digits in the given number is:", a)
    