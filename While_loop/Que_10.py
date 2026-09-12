# This program generates the Fibonacci series up to a given number of terms.

n = int(input("Enter a number: "))

a = 1
b = 1
c = 0

print(a)
print(b)

for i in range(2, n+1, 1):
    c = a + b
    a = b
    b = c
    print(c)
   