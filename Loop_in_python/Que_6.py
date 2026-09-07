#  print ap without using maths 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ap display karne ka program likho

n = int(input('Enter a number: '))

a = 4

for i in range(1, n+1, 1):
    print(a)
    a = a + 3
    