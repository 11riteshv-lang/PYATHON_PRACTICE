# display this Gp - 1,2,4,8,16,32..... upto n terms.

n = int(input('Enter a numbera: '))

a = 1

for i in range(1, n, 1):
    print(a)
    a *= 2