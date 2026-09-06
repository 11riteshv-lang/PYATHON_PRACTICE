# print the total sum of numbers from 1 to n

n = int(input('Enter a number: '))
sum = 0
for i in range(1, n+1, 1):
    sum = sum + i
    print(sum)
    
print("Total sum is:", sum)