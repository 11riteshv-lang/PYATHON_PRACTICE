# 1,-2,3,-4,5,-6,7,-8,9,10...................... nth terms
     # ye Qution ache se samajao properly

n = int(input("Enter a number: "))

x = 0
y = 0

for i in range(1, n + 1, 1):
    if i % 2 == 0:
        y = y - i
    elif i % 2 != 0:
        x = x + i
    
print("The sum of the series is: ", x + y)
