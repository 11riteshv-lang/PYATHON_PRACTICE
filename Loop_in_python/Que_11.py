# display gp without using maths 100, 50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.1953125 gp display karne ka program likho
n = int(input('Enter a number: '))

a = 100

for i in range(1, n+1, 1):
    print(a, end=' ')
    a = a / 2