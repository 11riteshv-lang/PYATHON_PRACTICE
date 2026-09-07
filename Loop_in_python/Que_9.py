#  gp without using maths 3, 12, 48, 192, 768, 3072, 12288, 49152, 196608, 786432 gp display karne ka program likho

n = int(input('Enter a number: '))

a = 3

for i in range(1, n+1, 1):
    print(a, end=' ')
    a = a * 4