#  ap qution without using maths 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ap display karne ka program likho

n = int(input('Enter a number: '))

a = 1

for i in range(1, n+1, 1):
    print(a, end=' ')
    a = a + 2