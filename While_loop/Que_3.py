# This program calculates the sum of the digits in a given number using a while loop.

# n = int(input("Enter a number: "))

# Total_sum = 0
# Last_digit = 0

# while n != 0:
#     Last_digit = n % 10
#     Total_sum = Total_sum + Last_digit
#     n = n // 10

# print("The sum of the digits in the given number is:", Total_sum)



n = int(input("Enter a number: "))

last_digit = 0
count = 0

while n != 0:
    last_digit = n % 10
    count = count + last_digit
    n = n // 10

print("The sum of the digits in the given number is:", count)
    






