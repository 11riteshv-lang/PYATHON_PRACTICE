# while loop to find the sum of even digits in a number

n = int(input("Enter a number: "))

last_digit = 0
Total_Even_Sum = 0


while n != 0:
    last_digit = n % 10
    if last_digit % 2 == 0:
        Total_Even_Sum = Total_Even_Sum + last_digit
    n = n // 10

print("The sum of the even digits in the given number is:", Total_Even_Sum)
        
    
    
    
    
    
    
    