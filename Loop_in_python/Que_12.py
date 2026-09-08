# Program to check if a number is prime or not

n = int(input('Enter a number: '))

if n <= 1:
    print("1 is Neither prime or nor composite")
else:
    for i in range(2, n, 1):
        if n % i == 0:
            print("It is not prime number ")
            break
    else:
        print("It is prime number") 