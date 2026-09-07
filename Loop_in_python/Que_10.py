# display ap without using maths 100, 97, 94, 91, 88, 85, 82, 79, 76, 73 ap display karne ka program likho

n = int(input('Enter a number: '))

a = 100

for i in range(1, n+1, 1):
    if a >= 0:
        print(a, end=' ')
        a = a - 3   
        
    
    