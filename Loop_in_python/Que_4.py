# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ap display karne ka program likho

n = int(input('Enter a number: '))

for i in range (1, 2*(n+1), 2):
    print(i, end=' ')