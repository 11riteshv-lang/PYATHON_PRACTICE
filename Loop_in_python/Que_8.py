# print gp without using maths 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 gp display karne ka program likho

n = int(input('Enter a number: '))

a = 1

for i in range(1, n+1, 1):
    print(a, end=' ')
    a = a * 2