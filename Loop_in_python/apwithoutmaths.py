# 4,7,10,13,16,.......upto n terms__________... without using maths.

n = int(input("Enter a number: "))

x = 4
for i in range(1, n, 1):
    print(x)
    x += 3